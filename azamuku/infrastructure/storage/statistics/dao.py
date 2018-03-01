# coding: utf-8

from pymongo import MongoClient

from domain.entities import ClickStatistics
from domain.interfaces import IClickStatisticsDAO

from .serializers import ClickStatisticsSerializer


class MongoClickStatisticsDAO(IClickStatisticsDAO):

    def __init__(self, mongo_uri: str):
        self.serializer = ClickStatisticsSerializer()
        self.client = MongoClient(mongo_uri)
        self.collection = self.client.azamuku.click_statistics

    def insert(self, click_statistics: ClickStatistics) -> None:
        click_dict = self.serializer.dump(click_statistics).data
        self.collection.insert_one(click_dict)

    def clean(self):
        self.collection.delete_many({})
