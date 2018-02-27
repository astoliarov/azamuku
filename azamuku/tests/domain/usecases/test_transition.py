# coding: utf-8

from unittest import mock

from domain.entities import ShortenedLink
from domain.usecases.transition import TransitionUseCase

from tests.utils.test_cases import BaseUnitTestCase


class LinkShorteningTestCase(BaseUnitTestCase):

    def setUp(self):

        self.shortened_dao = mock.Mock()
        self.click_statistics_dao = mock.Mock()

        self.use_case = TransitionUseCase(
            shortened_link_dao=self.shortened_dao,
            click_statistics_dao=self.click_statistics_dao,
        )

        self.shortened_link = ShortenedLink(
            target_link='awesome link',
            key='awesome key'
        )

    def test__execute__shortened_link_called(self):
        self.shortened_dao.get_by_key.return_value = self.shortened_link

        self.use_case.execute(
            key=self.shortened_link.key
        )

        self.shortened_dao.get_by_key.assert_called_once_with(self.shortened_link.key)

    def test__execute__not_found__no_key(self):

        self.shortened_dao.get_by_key.return_value = None

        response = self.use_case.execute(
            key=self.shortened_link.key
        )

        self.assertFalse(response.is_target_url_founded)
        self.assertIsNone(response.target_link)

    def test__execute__success__got_target_link(self):

        self.shortened_dao.get_by_key.return_value = self.shortened_link

        response = self.use_case.execute(
            key=self.shortened_link.key
        )

        self.assertTrue(response.is_target_url_founded)
        self.assertIsNotNone(response.target_link)

    def test__execute__success__target_url_correct(self):

        self.shortened_dao.get_by_key.return_value = self.shortened_link

        response = self.use_case.execute(
            key=self.shortened_link.key
        )

        self.assertEqual(response.target_link, self.shortened_link.target_link)

    def test__execute__success__statistics_inserted(self):

        self.shortened_dao.get_by_key.return_value = self.shortened_link

        response = self.use_case.execute(
            key=self.shortened_link.key
        )

        self.click_statistics_dao.insert.assert_called_once()

    def test__execute__success__statistics_collected(self):
        user_ip = '192.168.0.1'
        user_agent = 'Awesome agent'
        referer = 'awesome referer'

        self.shortened_dao.get_by_key.return_value = self.shortened_link

        response = self.use_case.execute(
            key=self.shortened_link.key,
            user_ip=user_ip,
            user_agent=user_agent,
            referer=referer,
        )

        args, _ = self.click_statistics_dao.insert.call_args
        click_statistics = args[0]

        self.assertEqual(click_statistics.user_ip, user_ip)
        self.assertEqual(click_statistics.user_agent, user_agent)
        self.assertEqual(click_statistics.referer, referer)
        self.assertEqual(click_statistics.click_key, self.shortened_link.key)
        self.assertEqual(click_statistics.target_link, self.shortened_link.target_link)

