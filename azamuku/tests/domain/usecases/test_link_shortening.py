# coding: utf-8
from unittest import mock

from domain.entities.shortened_link import ShortenedLink
from domain.usecases.link_shortening import LinkShorteningUseCase

from tests.utils.test_cases import BaseUnitTestCase


class LinkShorteningTestCase(BaseUnitTestCase):

    def setUp(self):

        self.shortened_dao = mock.Mock()
        self.key_generation_service = mock.Mock()

        self.use_case = LinkShorteningUseCase(
            shortened_link_dao=self.shortened_dao,
            key_generation_service=self.key_generation_service
        )

    def test__execute__return_shortened_link_object(self):
        generated_key = 'awesome key'
        target_link = 'awesome link'

        self.key_generation_service.generate.return_value = generated_key

        shortened_link = self.use_case.execute(target_link)

        self.assertTrue(isinstance(shortened_link, ShortenedLink))

    def test__execute__shortened_link_builded_correctly(self):
        generated_key = 'awesome key'
        target_link = 'awesome link'

        self.key_generation_service.generate.return_value = generated_key

        shortened_link = self.use_case.execute(target_link)

        self.assertEqual(shortened_link.target_link, target_link)
        self.assertEqual(shortened_link.key, generated_key)

