
from datetime import date

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade < 18:
    print(f"Você ainda não atingiu a maioridade. Faltam {18 - idade} anos para você completar 18 anos.")