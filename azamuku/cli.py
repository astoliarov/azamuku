# coding: utf-8

import fire

from application import Azamuku


class Cli:

    def __init__(self):
        self.azamuku = Azamuku()

    def __str__(self) -> str:
        return "Azamuku command-line interface"

    def shell(self):
        pass


if __name__ == '__main__':
    fire.Fire(Cli)
