print('\n') # Início do exercício

# Exercício 036: Gerenciador de Pagamentos

print('\033[33m=-' * 19 + ' Gerenciador de Pagamentos ' + '-=' * 19 + '\033[m')
casa = float(input('Qual o valor da casa?: R$ \033[32m'))
salario = float(input('\033[mQual o salário do comprador?: R$ \033[32m'))
anos = int(input('\033[mEm quantos anos pretende financiar?: \033[32m'))
print('\033[m')

# Cálculo da prestação mensal

prestacao = casa / (anos * 12)
print('\033[33m-\033[m' * 103)
print(f'Para pagar uma casa de R$ \033[32m{casa:.2f}\033[m em \033[32m{anos}\033[m anos, a prestação mensal será de R$ {prestacao:.2f}')

# Verificação se a prestação mensal ultrapassa 30% do salário

if prestacao > (salario * 0.3):
    print(F'Empréstimo \033[31mNEGADO!\033[m A prestação de R$ {prestacao:.2f} ultrapassa 30% do seu salário.')
else:
    print(F'Empréstimo \033[32mAPROVADO!\033[m A prestação de R$ {prestacao:.2f} está dentro do limite de 30% do seu salário.')
    
print('\033[33m-' * 103 + '\033[m')
print('\n')

# Fim do exercício