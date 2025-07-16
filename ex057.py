 # ex057

s = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while s != 'M':    
    s = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()
    while s != 'F':
        s = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()
if s == 'M':
    print('Sexo "MASCULINO" registrado com sucesso!')
elif s == 'F':
    print('Sexo "FEMININO" registrado com sucesso!')