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
    if jogador == 3:
        print('\033[1;31mVocê saiu do jogo!\033[m')
        print('\n')
        exit()
    elif jogador < 0 or jogador > 3:
        print('\033[1;31mJOGADA INVÁLIDA! TENTE NOVAMENTE.\033[m')
        print('\n')
        escolha_jogador()

def escolha_computador():
    global computador
    computador = random.randint(0, 2)


def esperar():
    sleep(0.5)
    print('\033[1;33mJO')
    sleep(1)
    print('\033[1;32mKEN')
    sleep(1)
    print('\033[1;34mPÔ!!!\033[m')
    print('\n')
   
    
def verifica_jogada():
    global resultado
    if jogador == computador:
        resultado = '\033[1;32mEMPATOU!\033[m'
    elif jogador == 0 and computador == 1:
        resultado = 'O JOGADOR \033[1;31mPERDEU!\033[m'
    elif jogador == 0 and computador == 2:
        resultado = 'O JOGADOR \033[1;32mGANHOU\033[m'
    elif jogador == 1 and computador == 0:
        resultado = 'O JOGADOR \033[1;32mGANHOU\033[m'
    elif jogador == 1 and computador == 2:
        resultado = 'O JOGADOR \033[1;31mPERDEU!\033[m'
    elif jogador == 2 and computador == 0:
        resultado = 'O JOGADOR \033[1;31mPERDEU!\033[m'
    elif jogador == 2 and computador == 1:
        resultado = 'O JOGADOR \033[1;32mGANHOU\033[m'
    elif jogador == 3:
        resultado = 'O JOGADOR \033[1;31mSAIU DO JOGO!\033[m'
    else:
        resultado = 'JOGADA INVÁLIDA! TENTE NOVAMENTE.'

def descricao_jogada():
    global jogador, computador
    print('=' * 69)
    print(f'Jogador escolheu: {opcoes[jogador]}')
    print(f'Computador escolheu: {opcoes[computador]}')
    print('=' * 69)
    print('\n')
    print(resultado)
    print('\n')

def main():
    limpa_tela()
    cabecalho()
    escolha_jogador()
    escolha_computador()
    esperar()
    verifica_jogada()
    descricao_jogada()
    print('\n\033[1;33mObrigado por jogar!\033[m')
    print('\033[1;33mVolte sempre!\033[m')
    print('\n' + '=' * 69)
    
main()
