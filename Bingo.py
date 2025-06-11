# Bingo 
import os
def limpa():
    """
    Limpa a tela do terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')    

# Chama a função limpa para limpar a tela ao iniciar o jogo

def exibe_menu():
    """
    Exibe o menu principal do jogo Bingo.
    """
    limpa() # Chama a função limpa para limpar a tela ao iniciar o jogo
    print("-=" * 46)
    print("-=" * 20, "Bingo Game", "-=" * 20)
    print("-=" * 46)
    print(" " * 38 + "Menu Jogo Bingo\n")
    print("Escolha uma opção:\n")
    print("1. Iniciar Jogo")
    print("2. Regras do Jogo")
    print("3. Sair")

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
exibe_menu()
opção = input("\nDigite a opção desejada: ")
if opção == '1':
    main()