# coding: utf-8
import hashlib

from domain.interfaces import IKeyGenerationService


class KeyGenerationService(IKeyGenerationService):

    def generate(self, target_url: str) -> str:

        target_bytes = target_url.encode('utf-8')

        hex_value = hashlib.sha1(target_bytes).hexdigest()
        return hex_value[:5]


