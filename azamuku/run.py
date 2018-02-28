# coding: utf-8

from domain.entities import ShortenedLink
from infrastructure.storage.shortened_link.dao import  RedisShortenedLinkDAO



link = ShortenedLink('test', 'test')
dao = RedisShortenedLinkDAO('redis://redis:6379/')

dao.upsert(link)
print(dao.get_by_key(link.key))
