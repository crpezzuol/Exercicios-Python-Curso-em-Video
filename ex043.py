print('\n')
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (mts): '))
print('\n')
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC está em {imc:.1f} CUIDADO! você está ABAIXO DO PESO!')
elif imc < 25:
    print(f'Seu IMC está em {imc:.1f} e você está de PARABÉNS seu peso está NORMAL!')
elif imc < 30:
    print(f'Seu IMC está em {imc:.1f} e você tem que se CUIDAR porque está com SOBREPESO!')
elif imc < 40:
    print(f'Seu IMC está em {imc:.1f} CUIDADO! você está OBESO!')
else:
    print(f'Seu IMC está em {imc:.1f} CUIDADO! você está com OBESIDADE MÓRBIDA!')
print('\n')