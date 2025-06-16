# This program compares two numbers input by the user.
# This program will have two versions: English and Portuguese from Brazil.

# Este programa compara dois números inseridos pelo usuário.
# Este programa irá ter duas versões Inglês e Português do Brasil


# Importing the os module to clear the screen
# Importando o módulo os para limpar a tela
import os

# This function clears the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Esta função limpa a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# This function prompts the user to choose a version of the program.
def option_version():
    clear_screen()
    print('\033[1;33m-=' * 36)
    print('\033[1;33m-' * 25,'\033[1;34mVersion  Information\033[1;33m', 25 * '-')
    print('\033[1;33m-=' * 36)
    print('\033[m')
    print('\033[1;33mThis program has two versions:\033[m\n')
    print('\033[1;33m1. English Version\033[m')
    print('\033[1;33m2. Portuguese Brazil Version\033[m')
    print('\033[m')
    global choice
    choice = int(input('\033[1;33mPlease choose a version by entering the corresponding number: \033[32m'))
    print('\033[m')

# This function prints a header message to introduce the program.
def print_header():
    print('\033[1;33m-=' * 36)
    print('\033[1;33m-' * 23,'\033[1;34mNumber Comparison Program\033[1;33m', 22 * '-')
    print('\033[1;33m-=' * 36)
    print('\033[m')

# Esta função imprime uma mensagem de cabeçalho para apresentar o programa.
def imprimir_cabecalho():
    print('\033[1;33m-=' * 40)
    print('\033[1;33m-' * 23,'\033[1;34mPrograma de Comparação de Números\033[1;33m', 22 * '-')
    print('\033[1;33m-=' * 40)
    print('\033[m')


# This function prints instructions for the user on how to use the program.
def print_instructions():
    print('\033[1;33mPlease enter two numbers to compare them.\033[m')
    print('\033[1;33mThe program will tell you which number is greater, or if they are equal.\033[m')
    print('\033[m')

# Esta função imprime instruções para o usuário sobre como usar o programa.
def imprimir_instrucoes():
    print('\033[1;33mPor favor, insira dois números para compará-los.\033[m')
    print('\033[1;33mO programa informará qual número é maior ou se são iguais.\033[m')
    print('\033[m')

# Prompt the user to enter two numbers
def prompt_user(): 
    global n1, n2
    n1 = float(input("Enter first number: \033[32m"))
    n2 = float(input("\033[mEnter second number: \033[32m"))
    print('\033[m')

# Solicitar ao usuário que insira dois números
def solicitar_usuario():
    global n1, n2
    n1 = float(input("Digite o primeiro número: \033[32m"))
    n2 = float(input("\033[mDigite o segundo número: \033[32m"))
    print('\033[m')

# Compare the two numbers and print the result 
def compare_numbers(n1, n2):
    if n1 > n2:
        print(f"The first number \033[32m{n1}\033[m is greater than the second number \033[31m{n2}\033[m")
    elif n1 < n2:
        print(f"The second number \033[32m{n2}\033[m is greater than the first number \033[31m{n1}\033[m")
    else:
        print(f"The two numbers are equal: \033[32m{n1}\033[m = \033[32m{n2}\033[m")
    print('\n')
# Comparar os dois números e imprimir o resultado
def comparar_numeros(n1, n2):
    if n1 > n2:
        print(f"O primeiro número \033[32m{n1}\033[m é maior que o segundo número \033[31m{n2}\033[m")
    elif n1 < n2:
        print(f"O segundo número \033[32m{n2}\033[m é maior que o primeiro número \033[31m{n1}\033[m")
    else:
        print(f"Os dois números são iguais: \033[32m{n1}\033[m = \033[32m{n2}\033[m")
    print('\n')

# This function prints a footer message to thank the user for using the program.
def print_footer():
    print('\033[1;33m-=' * 36)
    print('\033[1;34mThank you for using the number comparison program!\033[m')
    print('\033[1;33m-=' * 36)
    print('\033[m')
    print('\n')

# Esta função imprime uma mensagem de rodapé para agradecer ao usuário por usar o programa.
def imprimir_rodape():
    print('\033[1;33m-=' * 40)
    print('\033[1;34mObrigado por usar o programa de comparação de números!\033[m')
    print('\033[1;33m-=' * 40)
    print('\033[m')
    print('\n')

# Main program execution English version
def main_english(): 
    clear_screen()
    print_header()
    print_instructions()
    prompt_user()
    compare_numbers(n1, n2)
    print_footer()

# Execução do programa principal versão em português
def main_portuquese():
    limpar_tela()
    imprimir_cabecalho()
    imprimir_instrucoes()
    solicitar_usuario()
    comparar_numeros(n1, n2)
    imprimir_rodape()

# Main function to run the program
def main():
    option_version()
    if choice == 1:
        main_english()
    elif choice == 2:
        main_portuquese()
    else:
        print("\033[31mInvalid choice. Please run the program again.\033[m")

# Run the main function to start the program
# Executar a função principal para iniciar o programa
main() 
