# Peça para o usuário digitar um número e informe se ele é múltiplo de 3 e/ou de 5.
numero = int(input("Digite um número: "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f"{numero} é múltiplo de 3 e de 5.")
elif numero % 3 == 0:
    print(f"{numero} é múltiplo de 3, mas não de 5.")
elif numero % 5 == 0:
    print(f"{numero} é múltiplo de 5, mas não de 3.")
else:
    print(f"{numero} não é múltiplo nem de 3 nem de 5.")
