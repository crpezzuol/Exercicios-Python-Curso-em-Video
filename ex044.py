import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpa_tela()

print('\033[1;32m<>\033[1;33m<>' * 5,'\033[1;34mLOJAS PEZZUOL','\033[1;32m<>\033[1;33m<>' * 5)
print('\n\033[m')
compras = float(input('Preço das compras: R$ \033[1;32m'))
print('\n\033[m')
pagamento = int(input('Qual a opção? \033[1;32m'))
