
from datetime import date

ano_nasc = int(input("Digite seu ano de nascimento: \033[32m"))
print('\033[m')
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f"Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.")
if idade == 18:
    print(f"Você tem que se alistar \033[31IMEDIATAMENTE!")
    print('\033[m')
elif idade < 18:
    print(f"Ainda faltam \033[31m{18 - idade} anos\033[m para você se alistar.")
    print('\033[m')