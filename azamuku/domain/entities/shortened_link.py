# coding: utf-8


class ShortenedLink:
    """
    ShortenedLink is an object that represents result of shortening
    """

    def __init__(
            self,
            target_link: str,
            key: str,
    ):
        self.target_link = target_link
        self.key = key
