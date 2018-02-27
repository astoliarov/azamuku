# coding: utf-8

from abc import ABCMeta, abstractmethod
from typing import Optional

from domain.entities import ClickStatistics, ShortenedLink


class IShortenedLinkDAO(metaclass=ABCMeta):

    @abstractmethod
    def upsert(self, link: ShortenedLink) -> None:
        pass

    @abstractmethod
    def get_by_key(self, key: str) -> Optional[ShortenedLink]:
        pass


class IClickStatisticsDAO(metaclass=ABCMeta):

    @abstractmethod
    def insert(self, click_statistics: ClickStatistics) -> None:
        pass


class IKeyGenerationService(metaclass=ABCMeta):

    @abstractmethod
    def generate(self, target_url: str) -> str:
        pass
