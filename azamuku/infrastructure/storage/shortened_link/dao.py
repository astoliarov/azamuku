# coding: utf-8

import redis

from domain.entities import ShortenedLink
from domain.interfaces import IShortenedLinkDAO

from .serializers import ShortenedLinkSerializer


class RedisShortenedLinkDAO(IShortenedLinkDAO):
    DATA_ENCODING = 'utf-8'

    def __init__(self, uri):
        self.serializer = ShortenedLinkSerializer()
        self.conn = redis.StrictRedis.from_url(uri)

    def upsert(self, link: ShortenedLink) -> None:

        obj_str = self.serializer.dumps(link).data
        obj_bytes = obj_str.encode(self.DATA_ENCODING)

        self.conn.set(link.key, obj_bytes)

    def get_by_key(self, key: str):

        obj_bytes = self.conn.get(key)
        if obj_bytes is None:
            return None

        obj_str = obj_bytes.decode(self.DATA_ENCODING)
        return self.serializer.loads(obj_str).data

    def clean(self):
        self.conn.flushall()

