# Bingo 
import os
def limpa():
    """
    Limpa a tela do terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')    

def regras():
    """
    Exibe as regras do jogo Bingo.
    """
    limpa() # Chama a função limpa para limpar a tela antes de exibir as regras
    print("-=" * 46)
    print("-=" * 18, "Regras  Jogo Bingo", "-=" * 18)
    print("-=" * 46)
    print("\n" * 2)
    print("Regras do Jogo Bingo:\n")
    print("1. O jogo é jogado com um cartão de Bingo que contém números.")
    print("2. Um número é sorteado aleatoriamente e anunciado.")
    print("3. Os jogadores marcam o número em seus cartões se estiver presente.")
    print("4. O primeiro jogador a completar uma linha, coluna ou diagonal ganha.")
    print("5. O jogo continua até que um jogador complete o cartão ou até que não haja mais números a serem sorteados.")
    print("\n" * 2 + "Boa sorte!\n")

def cabecalho():
    """
    Exibe o cabeçalho do jogo Bingo.
    """
    print("\033[1;33m-=" * 46)
    print("-=" * 20, "\033[1;32mBingo Game", "\033[1;33m-=" * 20)
    print("-=" * 46)
    print("\n\033[m" )

def exibe_menu():
    """
    Exibe o menu principal do jogo Bingo.
    """
    limpa() # Chama a função limpa para limpar a tela ao iniciar o jogo
    cabecalho()  # Chama a função cabeçalho para exibir o cabeçalho do jogo
    print("\033[1;33m>" * 37, "\033[1;32mMenu Jogo Bingo", '\033[1;33m<' * 38)
    print("\n")
    print("\033[1;32mEscolha uma opção:\n")
    print("\033[1;34m1. \033[mIniciar Jogo")
    print("\033[1;34m2. \033[mRegras do Jogo")
    print("\033[1;34m3. \033[mSair")
    escolha()

def main():
    """
    Função principal do jogo Bingo.
    """
    limpa()  # Chama a função limpa para limpar a tela antes de iniciar o jogo
    cabecalho()  # Chama a função cabeçalho para exibir o cabeçalho do jogo
    print('\033[1;33m>' * 32, "\033[1;32mBem-vindo ao jogo de Bingo!", '\033[1;33m<' * 31)
    # Aqui você pode adicionar a lógica do jogo de Bingo
    # Por exemplo, gerar cartões de Bingo, sortear números, etc.
    print("\n" * 2 + "\033[mVamos começar!\n")
    # Por exemplo, gerar números aleatórios, verificar vencedores, etc.
    print('\n\033[1;31mO jogo ainda não está implementado!')
    print('\n' * 2 + "\033[1;32mObrigado por jogar!")
    print("Volte sempre!")
    print('-=' * 46)
    print("\n" * 2)
    exit()

def escolha():
    opcao = input("\nDigite a opção desejada: \033[1;32m").strip()
    print("\033[m")  # Reseta a cor do texto após a entrada do usuário
    if opcao == '1':
        main()  
    elif opcao == '2':
        regras()
        input("\nPressione Enter para voltar ao menu principal... ")
        exibe_menu()
    elif opcao == '3':
        limpa()
        print('-=' * 46)
        print('\n' * 2)
        print('Saindo do jogo...')
        print("\n" * 2)
        print('-=' * 46)
        print("\n" * 2)
        print("Obrigado por jogar! Até a próxima!", "\n" * 3)
        print('-=' * 46)
        print("\n" * 2)
        exit()


exibe_menu()  # Chama a função para exibir o menu principal ao iniciar o jogo    