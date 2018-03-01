# coding: utf-8

import json
import falcon

from domain.usecases.link_shortening import LinkShorteningUseCase


def init_web_app(
    link_shortening_use_case: LinkShorteningUseCase
) -> falcon.API:

    link_shortening_resource = LinkShorteningResource(link_shortening_use_case)

    web_app = falcon.API()
    web_app.add_route('/shorten', link_shortening_resource)
    return web_app


class LinkShorteningResource:

    def __init__(self, use_case: LinkShorteningUseCase):
        self.use_case = use_case

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        target_link = req.params.get('link')
        if target_link is None:
            resp.status = falcon.HTTP_403
            return

        shortened_link = self.use_case.execute(target_link)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'key': shortened_link.key})
        return
