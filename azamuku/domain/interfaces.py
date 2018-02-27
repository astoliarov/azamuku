# coding: utf-8

from abc import ABCMeta, abstractmethod

from domain.entities.shortened_link import ShortenedLink


class IShortenedLinkDAO(metaclass=ABCMeta):

    @abstractmethod
    def upsert(self, link: ShortenedLink) -> None:
        pass


class IKeyGenerationService(metaclass=ABCMeta):

    @abstractmethod
    def generate(self, target_url: str) -> str:
        pass