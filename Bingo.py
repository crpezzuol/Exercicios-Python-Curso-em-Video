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
    print("-=" * 18, "Bingo Game", "-=" * 18)
    print(" " * 10 + "Menu do Jogo Bingo")
    print("Menu do Jogo Bingo")
    print("1. Iniciar Jogo")
    print("2. Regras do Jogo")
    print("3. Sair")

def main():
    """
    Função principal do jogo Bingo.
    """
    print("Bem-vindo ao jogo de Bingo!")
    # Aqui você pode adicionar a lógica do jogo de Bingo
    # Por exemplo, gerar números aleatórios, verificar vencedores, etc.
    print("O jogo ainda não está implementado.")

exibe_menu()