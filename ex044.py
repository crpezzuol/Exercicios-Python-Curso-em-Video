import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpa_tela()

print('\033[1;32m<>\033[1;33m<>' * 10,'\033[1;34mLOJAS PEZZUOL','\033[1;32m<>\033[1;33m<>' * 10)
print('\n\033[m')
compra = float(input('Preço das compras: R$ \033[1;32m'))
print('\n\033[m')
print('''FORMAS DE PAGAMENTO >\n
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão
''')
pagamento = int(input('Qual a opção? \033[1;32m'))
print('\n\033[m')
if pagamento == 1:
    print(f'Sua compra de R$ {compra:.2f} com desconto de \033[1;32m" 10% "\033[m vai custar R$ \033[1;32m{compra * 0.9:.2f}\033[m no final.')
elif pagamento == 2:
    print(f'Sua compra de R$ {compra:.2f} com desconto de \033[1;32m" 5% "\033[m vai custar R$ \033[1;32m{compra * 0.95:.2f}\033[m no final.')
elif pagamento == 3:
    print(f'Sua compra de R$ {compra:.2f} \033[1;31m" SEM "\033[m desconto vai custar R$ \033[1;32m{compra:.2f}\033[m.')

print('\n\033[m')