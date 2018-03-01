# coding: utf-8

from marshmallow import fields, Schema, post_load

from domain.entities import ClickStatistics


class ClickStatisticsSerializer(Schema):

    click_key = fields.String(required=True)
    target_link = fields.String(required=True)

    referer = fields.String(required=True)
    user_agent = fields.String(required=True)
    user_ip = fields.String(required=True)

    click_datetime = fields.DateTime(required=True)

    @post_load
    def make_model(self, data):
        return ClickStatistics(**data)
