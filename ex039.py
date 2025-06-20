
from datetime import date

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
