import time
import json

try:
    
    from src.bloco import Bloco
    from src.bloco_minerado import BlocoMinerado

    from src.header import Header
    from src.payload import Payload
    from src.helpers import Helpers
except ImportError:
    print("Erro ao importar o módulo 'helpers'")

class Blockchain:

    def __init__(self, dificuldade: int = 4) -> None:
        self.__chain = []
        self.__prefixo_pow = '0'
        self.__dificuldade = dificuldade
        self.__chain.append(self.__criar_bloco_genesis())

    @property
    def chain(self) -> tuple[Bloco]:
        return tuple(self.__chain)

    def __criar_bloco_genesis(self):
        payload = Payload(0, time.time(), 'Bloco Inicial', '')
        header = Header(0, Helpers.hash(json.dumps(str(payload))))

        bloco_genesis = Bloco(header, payload)
        #print(f'Bloco Genesis ({bloco_genesis.payload.sequencia}) criado: {bloco_genesis}')

        return bloco_genesis

    def criar_bloco(self, dados: any):
        novo_bloco = Bloco(
            payload=Payload(
                sequencia=self.__ultimo_bloco().payload.sequencia + 1,
                timestamp=time.time(),
                dados=dados,
                hash_anterior=self.__hash_ultimo_bloco()
            )
        )

        #print(f'Bloco {novo_bloco.payload.sequencia} criado: {novo_bloco}')
        return novo_bloco

    def minerar_bloco(self, bloco: Bloco):
        nonce = 0
        inicio = time.time()

        while True:
            hash_bloco = Helpers.hash(json.dumps(str(bloco.payload)))
            hash_pow = Helpers.hash(hash_bloco + str(nonce))

            if Helpers.hash_validado(hash_pow, self.__prefixo_pow, self.__dificuldade):
                final = time.time()
                hash_reduzido = hash_bloco[:12]
                tempo_mineracao = (final - inicio) / 1000                
                print(f'Bloco {bloco.payload.sequencia} minerado em {tempo_mineracao}s. Hash {hash_reduzido} ({nonce} tentativas)')

                bloco_minerado = Bloco(Header(nonce, hash_bloco), bloco.payload)
                return BlocoMinerado(bloco_minerado=bloco_minerado, hash_mineracao=hash_pow, tempo_mineracao=tempo_mineracao)

            nonce += 1

    def enviar_bloco(self, bloco_minerado: Bloco) -> list[Bloco]:
        if self.__verificar_bloco(bloco_minerado):
            self.__chain.append(bloco_minerado)
            #print(f'Bloco {bloco_minerado.payload.sequencia} foi adicionado à blockchain: {bloco_minerado}')
        return self.__chain

    def __ultimo_bloco(self) -> Bloco:
        return self.__chain[-1]

    def __hash_ultimo_bloco(self) -> str:
        return self.__ultimo_bloco().header.hash_bloco

    def __verificar_bloco(self, bloco: Bloco) -> bool:
        if bloco.payload.hash_anterior != self.__hash_ultimo_bloco():
            #print(f'Bloco {bloco.payload.sequencia} inválido: O hash anterior é {self.__hash_ultimo_bloco()[:12]} e não {bloco.payload.hash_anterior[:12]}. ')
            return False

        hash_payload = Helpers.hash(json.dumps(str(bloco.payload)))
        hash_teste = Helpers.hash(hash_payload + str(bloco.header.nonce))
            
        if not Helpers.hash_validado(hash_teste, self.__dificuldade, self.__prefixo_pow):
            #print(f'Bloco {bloco.payload.sequencia} inválido: Nonce é {bloco.header.nonce} é inválido e não pode ser verificado')
            return False
        return True
