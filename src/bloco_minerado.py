import time
from src.bloco import Bloco


class BlocoMinerado:
    def __init__(self, bloco_minerado: Bloco, hash_mineracao:str, tempo_mineracao: time ) -> None:
        self.bloco_minerado = bloco_minerado
        self.hash_mineracao = hash_mineracao
        self.tempo_mineracao = tempo_mineracao