# coding: utf-8
import datetime

from domain.entities import ClickStatistics
from infrastructure.storage.statistics.dao import MongoClickStatisticsDAO

from tests.utils.test_cases import BaseIntegrationTestCase


class MognoClickStatisticsDAOTestCase(BaseIntegrationTestCase):

    def setUp(self):
        self.dao = MongoClickStatisticsDAO('mongodb://mongo:27017')
        self.dao.clean()

    def test__dao__insert__successful(self):

        click_statistics = ClickStatistics(
            click_datetime=datetime.datetime.now(),
            click_key='test',
            target_link='test',

            referer='test',
            user_agent='test',
            user_ip='192.168.0.1',
        )

        self.assertEqual(self.dao.collection.find().count(), 0)

        self.dao.insert(click_statistics)

        self.assertEqual(self.dao.collection.find().count(), 1)
