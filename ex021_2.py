import pygame
import os

# Inicializa o pygame
pygame.init()
# Inicializa o mixer do pygame
pygame.mixer.init()

# Função para tocar a música
def tocar_musica(musica):
    # Carrega a música
    pygame.mixer.music.load(musica)
    # Toca a música
    pygame.mixer.music.play()
    # Aguarda até que a música termine
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # Para o mixer
    pygame.mixer.quit()
# Função para parar a música
def parar_musica():
    pygame.mixer.music.stop()
    pygame.mixer.quit() 
# Função para pausar a música
def pausar_musica():
    pygame.mixer.music.pause()
# Função para continuar a música
def continuar_musica():
    pygame.mixer.music.unpause()    

# Definindo a função limpar_tela para limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def comando():
    print('Digite "p" para pausar a música')
    print('Digite "c" para continuar a música')
    print('Digite "s" para parar a música')
    print('Digite "m" para voltar ao menu')
    print('Digite "0" para sair do programa\n')
    comando = input('Digite o comando desejado: ')
    if comando == 'p':
        pausar_musica()
        comando()
    elif comando == 'c':
        continuar_musica()
        comando()
    elif comando == 's':
        parar_musica()
        menu()
    elif comando == 'm':
        menu()
    elif comando == '0':
        exit()
    else:
        print('\nComando inválido! Tente novamente.\n')

limpar_tela() 

def menu():
    print(10*'-', 'Escolha uma Musica', 10*'-','\n')
    print('1 - ALELUIA')
    print('2 - DÁ-ME TEUS OLHOS') 
    print('3 - JESUS FILHO DE DAVI')
    print('4 - BEA MILLER')
    print('5 - JADE FACER')
    print('0 - Sair\n')     
    print('Digite o número da música ' \
    'desejada: => ',end='')
    opcao = input() 
    if opcao == '1':
        tocar_musica('ex021_1.mp3')
        comando()
        #chama a função comando para executar os comandos
    elif opcao == '2':
        tocar_musica('ex021_2.mp3')
        comando()
        #chama a função comando para executar os comandos   
    elif opcao == '3':
        tocar_musica('ex021_3.mp3')
        comando()
        #chama a função comando para executar os comandos
    elif opcao == '4':
        tocar_musica('ex021_4.mp3')
        comando()
        #chama a função comando para executar os comandos
    elif opcao == '5':
        tocar_musica('ex021_5.mp3')
        comando()
        #chama a função comando para executar os comandos
    elif opcao == '0':
        print('\nSaindo do programa...\n')
        exit()
    else:
        print('\nOpção inválida! Tente novamente.\n')
menu()