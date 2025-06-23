print('\n')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
print('\n')
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC está em {imc:.2} CUIDADO! você está ABAIXO DO PESO!')
elif imc < 25:
    print(f'Seu IMC está em {imc:.2} e você está de PARABÉNS seu peso está NORMAL!')
elif imc < 30:
    print(f'Seu IMC está em {imc:.2} e você tem que se CUIDAR porque está com SOBREPESO!')
elif imc < 40:
    print(f'Seu IMC está em {imc:.2} CUIDADO! você está OBESO!')
else:
    print(f'Seu IMC está em {imc:.2} ') está