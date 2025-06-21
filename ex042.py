import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

s1 = int(input('Primeiro segmento: \033[32m'))
s2 = int(input('\033[mSegundo segmento: \033[32m'))
s3 = int(input('\033[mTerceiro segmento: \033[32m'))

