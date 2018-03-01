# coding: utf-8

from datetime import datetime


class ClickStatistics:
    """
    This model represents statistics that collected when user clicks on a shortened link
    """

    def __init__(
        self,
        click_key: str,
        target_link: str,

        click_datetime: datetime,

        referer: str='',
        user_agent: str='',
        user_ip: str='',
    ):
        self.click_key = click_key
        self.target_link = target_link
        self.referer = referer
        self.user_agent = user_agent
        self.user_ip = user_ip
        self.click_datetime = click_datetime
