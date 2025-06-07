# Ask the user to enter a number and tell whether it is even or odd.
# Peça para o usuário digitar um número e diga se ele é par ou ímpar
num = int(input("Enter a number: "))
if num % 2 == 0:
    print('The number is even!')
else:
    print('The number is odd!')

'''
Entendendo o Verificador de Número Par ou Ímpar
Esse código Python é bem simples e direto, ele serve para descobrir se um número que você digitou é par ou ímpar.

Vamos ver cada parte:

Python

numero = int(input('Enter a number: '))
input('Enter a number: '): Essa parte pede para você "Enter a number:" e espera que você digite algo no teclado e aperte Enter. O que você digitar, por padrão, é lido como um texto (uma string).
int(...): Como a gente quer fazer contas com esse valor, a função int() é usada para converter o texto que você digitou em um número inteiro. Se você digitar "5", por exemplo, int() transforma o texto "5" no número 5.
numero = ...: O número inteiro que você digitou é guardado na variável chamada numero.
Python

if numero % 2 == 0:
numero % 2: Essa é a parte mais importante para entender a lógica. O símbolo % é o operador de módulo. Ele calcula o resto da divisão de numero por 2.
Por exemplo, se numero for 4: 4 % 2 é 0 (quatro dividido por dois dá dois, e o resto é zero).
Se numero for 5: 5 % 2 é 1 (cinco dividido por dois dá dois, e o resto é um).
== 0: Aqui, o código está verificando se o resto da divisão por 2 é igual a zero.
Python

    print('The number is even!')
else:
    print('The number is odd!')
if numero % 2 == 0:: Se o resto da divisão por 2 for igual a zero, significa que o número é par.
print('The number is even!'): Nesse caso, a mensagem "The number is even!" é mostrada na tela.
else:: Se a condição acima for falsa (ou seja, o resto da divisão por 2 não for zero, ele será 1).
print('The number is odd!'): Então, a mensagem "The number is odd!" é exibida.
Em Resumo
O código pede um número, converte ele para um formato que dá pra fazer conta, e depois usa o resto da divisão por 2 pra saber se ele é par (resto zero) ou ímpar (resto um). É uma forma super eficiente e comum de fazer essa checagem em programação!
'''