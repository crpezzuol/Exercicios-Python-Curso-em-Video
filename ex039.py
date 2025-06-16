
from datetime import date

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade < 18:
    print(f"Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.")