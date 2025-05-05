import math
oposto = float(input('\nDigite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print(f'\nA hipotenusa vai medir: {hipotenusa:.2f}\n')