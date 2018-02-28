# coding: utf-8

from domain.entities import ShortenedLink
from infrastructure.storage.shortened_link.dao import RedisShortenedLinkDAO

from tests.utils.test_cases import BaseIntegrationTestCase


class RedisShortenedLinkDAOTestCase(BaseIntegrationTestCase):
    redis_uri = 'redis://redis:6379/'

    def setUp(self):
        self.dao = RedisShortenedLinkDAO(self.redis_uri)
        self.dao.clean()

    def test__get_by_key__nothing_found(self):
        result = self.dao.get_by_key('test')

        self.assertIsNone(result)

    def test__upsert_and_get__insert_successfully(self):
        link = ShortenedLink('test', 'test')

        self.dao.upsert(link)

        getted_link = self.dao.get_by_key(link.key)

        self.assertTrue(link == getted_link)





