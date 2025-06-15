# Exemplo de condicionais

nome = str(input('Qual é o seu nome?: '))

# Verifica o nome e imprime uma mensagem personalizada

if nome == 'Meire' or nome == 'Carlos' or nome =='Natan':
    print('Que nome bonito você tem!')
elif nome == 'Gustavo':
    print('Seu nome é bem FEIO!')
elif nome == 'João' or nome == 'Pedro' or nome == 'Maria' or nome == 'Aparecida':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')
