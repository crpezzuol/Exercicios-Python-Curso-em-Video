distancia = float(input("Qual é a distância da sua viagem? "))
print(f'Você está prestes a começar uma viagem de {distancia} km.')
if distancia <= 200:
    print('E o preço da sua passagem será de R$ 75.00')
else:
    print('E o preço de sua passagem será de R$ 94.50')
