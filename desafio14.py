# Peça para o usuário digitar uma frase e informe se ela é um palíndromo (lê-se igual de trás para frente, desconsiderando espaços)
frase = input("Digite uma frase: ").replace(" ", "").lower()

'''
frase = input('Digite uma frase: ').replace(' ', '').lower()
if frase == frase[::-1]:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')
'''