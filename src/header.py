import json


class Header:
    def __init__(self, nonce: int = 0, hash_bloco: str = '') -> None:
        self.nonce = nonce
        self.hash_bloco = hash_bloco

    def __str__(self):
        return json.dumps(self.__dict__, indent=2)