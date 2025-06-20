from datetime import date
import os


print('\n')
ano_nasc = int(input('Ano de Nascimento: \033[32m'))
print('\33[m')
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'O atleta tem {idade} anos.')
if idade < 10:
    print('Classificação: \033[1;34mMIRIM\033[m')
elif idade < 15:
    print('Classificação: \033[1;34mINFANTIL\033[m')
elif idade < 20:
    print('Classificação: \033[1;34mMIRIM\033[m')
