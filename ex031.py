distancia = float(input("Qual é a distância da sua viagem? "))
print(f'Você está prestes a começar uma viagem de {distancia} km.')
'''Verificando o preço da passagem...')
if distancia <= 200:
    print(f'E o preço da sua passagem será de R$ {distancia * 0.50:.2f}')
else:
    print(f'E o preço de sua passagem será de R$ {distancia * 0.45:.2f}')
'''
# Usando o operador ternário para simplificar a lógica
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será de R$ {preco:.2f}')