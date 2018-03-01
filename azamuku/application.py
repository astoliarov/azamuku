# coding: utf-8

import falcon

from domain.usecases.transition import TransitionUseCase
from domain.usecases.link_shortening import LinkShorteningUseCase

from infrastructure.http.routes import init_web_app
from infrastructure.storage.shortened_link.dao import RedisShortenedLinkDAO
from infrastructure.storage.statistics.dao import MongoClickStatisticsDAO
from infrastructure.utils.key_generation_service import KeyGenerationService


class Azamuku:

    def __init__(self):

        self.shortening_link_dao = RedisShortenedLinkDAO('redis://redis:6379/')
        self.click_statistics_dao = MongoClickStatisticsDAO('mongodb://mongo:27017')

        self.key_generation_service = KeyGenerationService()

        self.transition_use_case = TransitionUseCase(
            click_statistics_dao=self.click_statistics_dao,
            shortened_link_dao=self.shortening_link_dao
        )

        self.link_shortening_use_case = LinkShorteningUseCase(
            shortened_link_dao=self.shortening_link_dao,
            key_generation_service=self.key_generation_service
        )

        self.web_app = init_web_app(
            self.link_shortening_use_case
        )


