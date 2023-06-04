import json
from src.header import Header
from src.payload import Payload


class Bloco:
    def __init__(self, header: Header = None, payload: Payload = None) -> None:
        self.header = header
        self.payload = payload

    def __str__(self):
        return json.dumps({
            "header": str(self.header),
            "payload": str(self.payload)
        }, indent=2)