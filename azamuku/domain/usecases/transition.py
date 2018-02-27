# coding: utf-8
from datetime import datetime
from typing import Optional

from domain.entities import ClickStatistics
from domain.interfaces import IShortenedLinkDAO, IClickStatisticsDAO


class TransitionResponse:

    def __init__(
        self,
        is_target_url_founded: bool,
        target_link: Optional[str]=None
    ):
        self.is_target_url_founded = is_target_url_founded
        self.target_link = target_link


class TransitionUseCase:

    def __init__(
        self,
        shortened_link_dao: IShortenedLinkDAO,
        click_statistics_dao: IClickStatisticsDAO,
    ):
        self.shortened_link_dao = shortened_link_dao
        self.click_statistics_dao = click_statistics_dao

    def execute(self, key: str, referer: str='', user_agent: str='', user_ip: str=''):

        shortened_link = self.shortened_link_dao.get_by_key(key)
        if shortened_link is None:
            return TransitionResponse(is_target_url_founded=False)

        click_datetime = datetime.now()

        click_statistics = ClickStatistics(
            click_key=key,
            target_link=shortened_link.target_link,

            referer=referer,
            user_agent=user_agent,
            user_ip=user_ip,

            click_datetime=click_datetime
        )

        self.click_statistics_dao.insert(click_statistics)

        return TransitionResponse(
            is_target_url_founded=True,
            target_link=shortened_link.target_link
        )
