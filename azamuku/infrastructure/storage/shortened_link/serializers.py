# coding: utf-8

from marshmallow import fields, Schema, post_load

from domain.entities import ShortenedLink


class ShortenedLinkSerializer(Schema):

    target_link = fields.String(required=True)
    key = fields.String(required=True)

    @post_load
    def make_model(self, data):
        return ShortenedLink(**data)
