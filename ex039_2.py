
from datetime import date
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')







def alistamento():
    print('\033[1;34m' + '-' * 47)
    print('-' * 13, 'ALISTAMENTO MILITAR', '-' * 13)
    print('-' * 47 + '\033[m')
    print('\n')
    ano_nasc = int(input("Digite seu ano de nascimento: \033[32m"))
    print('\033[m')
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    print(f"Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.")
    if idade == 18:
        print(f"Você tem que se alistar \033[31mIMEDIATAMENTE!")
        print('\033[m')
    elif idade < 18:
        print(f"Ainda faltam \033[31m{18 - idade}\033[m anos para você se alistar.")
        print(f"Seu alistamento será em \033[32m{ano_nasc + 18}\033[m.")
        print('\033[m')
    else:
        print(f"Você já deveria ter se alistado há \033[31m{idade - 18}\033[m anos.")
        print(f"Seu alistamento foi em \033[32m{ano_nasc + 18}\033[m.")
        print('\033[m')

def rodape():
    print('\033[1;34m' + '-' * 47)
    print('-' * 15, 'FIM DO PROGRAMA', '-' * 15)
    print('-' * 47 + '\033[m')
    print('\n')

# Main program execution
def main():
    limpa_tela
    alistamento()
    rodape()
    print('\n')

def run():
    main()  

def sexo():
    limpa_tela
    print('\033[1;34m' + '-' * 47)
    print('-' * 20, '\033[33mSEXO\033[m', '\033[34m-' * 21)
    print('-' * 47 + '\033[m')
    print('\n')
    sexo = input("Digite seu sexo (M/F): ").strip().upper()
    print('\n')
    while sexo not in ('M', 'F'):
        sexo = input("Opção inválida! Digite seu sexo (M/F): ").strip().upper()
        print('\n')
    if sexo == 'M':
        print("Você é do sexo \033[31mMASCULINO\033[m e precisa de \033[31mALISTAR!\033[m")
        t = input('Tecle <ENTER> para verificar o ano do seu \033[31mALISTAMENTO!\033[m ')
        alistamento()
    else:
        print("Você é do sexo \033[35mFeminino\033[m não precisa se \033[32mALISTAR!\033[m")
        print('\n')
        rodape()
    print('\n')
        


sexo()
