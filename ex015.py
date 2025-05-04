dia = int(input('\nQuantos dias alugados? '))
km = float(input('Quantos km rodados? '))
v = (dia * 60) + (km * 0.15)
print(f'O total a pagar é de R${v:.2f}\n')