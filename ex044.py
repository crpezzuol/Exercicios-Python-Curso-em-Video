import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpa_tela()

print('\033[1;32m<>\033[1;33m<>' * 10,'\033[1;34mLOJAS  PEZZUOL','\033[1;32m<>\033[1;33m<>' * 10)
print('\n\033[m')
compra = float(input('Preço das compras: R$ \033[1;32m'))
print('\n\033[m')
print('''FORMAS DE PAGAMENTO \033[1;34m>\033[m\n
    [ \033[1;33m1\033[m ] à vista dinheiro/cheque
    [ \033[1;33m2\033[m ] à vista cartão
    [ \033[1;33m3\033[m ] 2x no cartão 
    [ \033[1;33m4\033[m ] 3x ou mais no cartão
''')
pagamento = int(input('Qual a opção? \033[1;32m'))
print('\n\033[m')
if pagamento == 1:
    print(f'Sua compra de R$ {compra:.2f} com desconto de \033[1;32m" 10% "\033[m vai custar R$ \033[1;32m{compra * 0.9:.2f}\033[m no final.')
elif pagamento == 2:
    print(f'Sua compra de R$ {compra:.2f} com desconto de \033[1;32m" 5% "\033[m vai custar R$ \033[1;32m{compra * 0.95:.2f}\033[m no final.')
elif pagamento == 3:
    print(f'Sua compra de R$ {compra:.2f} \033[1;31m" SEM DESCONTO"\033[m vai custar R$ \033[1;32m{compra:.2f}\033[m.')
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas deseja pagar? \033[1;32m'))
    parc_juros = (compra * 1.2) / parcelas
    print(f'\n\033[mSua compra será parcelada em \033[1;34m{parcelas}X\033[m de R$ \033[1;31m{parc_juros:.2f} COM JUROS DE " 20% "\033[m.')
    print(f'Sua compra de R$ \033[1;32m{compra:.2f}\033[m vai custar R$ \033[1;31m{parcelas * parc_juros:.2f}\033[m no final.\n')
else:     
    print('\033[1;31mOpção de Pagamento INVÁLIDA! Tente Novamente!\033[m')

print('\n')
print('\033[1;32m<>\033[1;33m<>' * 24)
print('\n\033[m')
