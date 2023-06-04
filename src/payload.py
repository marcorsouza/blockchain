import json
import time


class Payload:
    def __init__(self, sequencia: int = 0, timestamp: time = None, dados: str = '', hash_anterior: str = '') -> None:
        self.sequencia = sequencia
        self.timestamp = timestamp
        self.dados: any = dados
        self.hash_anterior = hash_anterior

    def __str__(self):
        return json.dumps(self.__dict__, indent=2)