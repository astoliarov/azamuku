# coding: utf-8

from urllib import parse

from domain.entities.shortened_link import ShortenedLink
from domain.interfaces import IShortenedLinkDAO, IKeyGenerationService


class LinkShorteningUseCase:

    def __init__(
            self,
            shortened_link_dao: IShortenedLinkDAO,
            key_generation_service: IKeyGenerationService,
    ):
        self.shortened_link_dao = shortened_link_dao
        self.key_generation_service = key_generation_service

    def execute(self, target_link: str) -> ShortenedLink:
        """
        This method contains main business logic of URL shortening

        :param target_link: url that need to be shortened
        :return: ShortenedLink instance
        """

        # Here is a place to add some business features
        # For example check for banned domains or something

        link_key = self.key_generation_service.generate(target_link)

        shortened_link = ShortenedLink(target_link=target_link, key=link_key)

        self.shortened_link_dao.upsert(shortened_link)

        return shortened_link
