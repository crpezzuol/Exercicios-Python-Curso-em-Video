print('\n') # Início do exercício
# Exercício 036: Gerenciador de Pagamentos
print('=-' * 20 + ' Gerenciador de Pagamentos ' + '-=' * 20)
casa = int(input('Qual o valor da casa?: R$ \033[32m\033[m'))
salario = int(input('\033[mQual o salário do comprador?: R$ \033[32m'))
anos = int(input('\033[mEm quantos anos pretende financiar?: \033[32m'))
prestacao = casa / (anos * 12)
print('-' * 100)
print(f'Para pagar uma casa de R$ \033[32m{casa:.2f}\033[m em \033[32m{anos}\033[m anos, a prestação mensal será de R$ {prestacao:.2f}')
if prestacao > (salario * 0.3):
    print(F'Empréstimo negado! A prestação de R$ {prestacao:.2f} ultrapassa 30% do seu salário.')
else:
    print(F'Empréstimo aprovado! A prestação de R$ {prestacao:.2f} está dentro do limite de 30% do seu salário.')
print('-' * 100)
print('\n')
# Fim do exercício