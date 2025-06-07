# Peça para o usuário digitar sua idade e informe em qual faixa etária ele se encontra: criança (0-12), adolescente (13-17), adulto (18-59) ou idoso (60+)
idade = int(input("Digite sua idade: "))
if idade <= 12:
    print('Você é uma criança.')
elif idade >= 13 and idade <= 17:
    print('Você é um adolescente.')
elif idade >= 18 and idade <= 59:
    print('Você é um adulto.')
elif idade >= 60:
    print('Você é um idoso.')