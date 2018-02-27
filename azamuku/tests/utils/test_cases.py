# coding: utf-8

from unittest import TestCase

from .utils import attr


@attr("unit")
class BaseUnitTestCase(TestCase):
    pass
