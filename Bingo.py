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
    print("-=" * 20, "Regras do Jogo Bingo", "-=" * 20)
    print("-=" * 46)
    print("\n" * 2)
    print("Regras do Jogo Bingo:\n")
    print("1. O jogo é jogado com um cartão de Bingo que contém números.")
    print("2. Um número é sorteado aleatoriamente e anunciado.")
    print("3. Os jogadores marcam o número em seus cartões se estiver presente.")
    print("4. O primeiro jogador a completar uma linha, coluna ou diagonal ganha.")
    print("5. O jogo continua até que um jogador complete o cartão ou até que não haja mais números a serem sorteados.")
    print("\n" * 2 + "Boa sorte!\n")

def exibe_menu():
    """
    Exibe o menu principal do jogo Bingo.
    """
    limpa() # Chama a função limpa para limpar a tela ao iniciar o jogo
    print("-=" * 46)
    print("-=" * 20, "Bingo Game", "-=" * 20)
    print("-=" * 46)
    print("\n" * 2)
    print(" " * 38 + "Menu Jogo Bingo\n")
    print("Escolha uma opção:\n")
    print("1. Iniciar Jogo")
    print("2. Regras do Jogo")
    print("3. Sair")
    escolha()

def main():
    """
    Função principal do jogo Bingo.
    """
    print('\n' * 2 + "Bem-vindo ao jogo de Bingo!")
    # Aqui você pode adicionar a lógica do jogo de Bingo
    # Por exemplo, gerar números aleatórios, verificar vencedores, etc.
    print('\nO jogo ainda não está implementado.')
    print('\n' * 2 + "Obrigado por jogar!\n")
    print("Volte sempre!\n")

def escolha():
    opcao = input("\nDigite a opção desejada: ")
    if opcao == '1':
        main()  
    elif opcao == '2':
        regras()
        input("\nPressione Enter para voltar ao menu principal...")
        exibe_menu()
    elif opcao == '3':
        limpa()
        print('-=' * 46)
        print("\nSaindo do jogo...\n")
        print('-=' * 46)
        print("\n" * 2)
        print("Obrigado por jogar! Até a próxima!", "\n" * 3)
        exit()


exibe_menu()  # Chama a função para exibir o menu principal ao iniciar o jogo    