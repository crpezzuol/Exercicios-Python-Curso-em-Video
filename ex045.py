import os
import random
from time import sleep
# JOKENPÔ - Jogo do Pedra, Papel e Tesoura
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print('=' * 30, '\033[1;32mJOKENPÔ\033[m', '=' * 30)
    print('\n\033[m')
    print('''\033[1;34mSuas opções são:\033[m\n
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    [3] SAI FORA''')
    print('\n\033[m')

def escolha_jogador():
    global jogador
    jogador = int(input('Qual a sua jogada? \033[1;32m'))
    print('\033[m')

def escolha_computador():
    global computador
    computador = random.randint(0, 2)


def esperar():
    sleep(1)
    print('\033[1;33mJO')
    sleep(1)
    print('\033[1;32mKEN')
    sleep(1)
    print('\033[1;34mPÔ!!!\033[m')
    print('\n')
    print('=' * 69)
    
def verifica_jogada():
    global resultado
    if jogador == computador:
        resultado = '\033[1;32mEMPATOU!\033[m'
    elif jogador == 0 and computador == 1:
        resultado = 'O JOGADOR \033[1;31mPERDEU!\033[m'
    elif jogador == 0 and computador == 2:
        resultado = 'O JOGADOR \033[1;32mGANHOU\033[m'

def main():
    limpa_tela()
    cabecalho()
    escolha_jogador()
    escolha_computador()
    esperar()
    print(f'{opcoes[computador]}')
    print(f'\033[1;35m{opcoes[jogador]}\033[m')
    verifica_jogada()
    print(resultado)
    



main()
