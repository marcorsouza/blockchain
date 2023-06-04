from src.blockchain import Blockchain

dificuldade_input = input('Qual é a dificuldade? ')
dificuldade = int(dificuldade_input) if dificuldade_input != '' else 4
num_blocos_input = input('Quantidade de blocos? ')
num_blocos = int(num_blocos_input) if num_blocos_input != '' else 10
blockchain = Blockchain(dificuldade)

chain = blockchain.chain

for i in  range(0, num_blocos):
    print('--- CRIAR NOVO BLOCO (PAYLOAD) ---')
    bloco = blockchain.criar_bloco(f'Bloco {i+1}')
    
    print('--- MINERAR BLOCO ---')
    mine_info = blockchain.minerar_bloco(bloco)
    
    print('--- ENVIAR BLOCO ---')
    chain = blockchain.enviar_bloco(mine_info.bloco_minerado)

print('--- BLOCKCHAIN ---')
for bloco in chain:
    print(bloco)
