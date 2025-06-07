# Peça para o usuário digitar um número e diga se ele é primo.

num = int(input('Digite um número: '))
if num > 1:
    for i in range(2, num): # enteder o que é range(2, int(n**0.5) + 1)
        if num % i == 0:
            print(f'{num} não é primo.')
            break
    else:
        print(f'{num} é primo.')
else:
    print('Números menores ou iguais a 1 não são primos.')

    '''
Entendendo o Verificador de Números Primos
Primeiro, vamos lembrar o que é um número primo: é um número natural maior que 1 que só pode ser dividido por 1 e por ele mesmo, sem deixar resto. Por exemplo, 2, 3, 5, 7 são números primos.

Agora, vamos ao código:

Python

num = int(input('Digite um número: '))
input('Digite um número: '): Aqui, o programa pede para o usuário "Digite um número:" e espera que ele digite algo. O que for digitado é recebido como um texto (uma string).
int(...): Como queremos trabalhar com números, a função int() converte o texto que o usuário digitou em um número inteiro.
num = ...: Esse número inteiro é então guardado na variável chamada num.
Python

if num > 1:
if num > 1:: Esta linha verifica se o número que o usuário digitou é maior que 1. Por que isso? Porque, por definição, números primos são sempre maiores que 1. Se o número não for maior que 1, ele já não pode ser primo.
Python

    for i in range(2, num):
        if num % i == 0:
            print(f'{num} não é primo.')
            break
    else:
        print(f'{num} é primo.')
Essa é a parte principal do código, onde a "mágica" acontece:

for i in range(2, num):: Se o num for maior que 1, o programa entra nesse loop (laço de repetição). Ele vai começar a testar divisões a partir do número 2 (porque todo número é divisível por 1, e não precisamos testar isso) e vai até o número imediatamente anterior ao num que o usuário digitou.

A variável i vai assumir cada um desses valores (2, 3, 4, ..., até num - 1).
if num % i == 0:: Dentro do loop, essa linha faz a verificação crucial.

num % i: Isso é o operador de módulo. Ele calcula o resto da divisão de num por i.
== 0: Se o resto da divisão for 0, significa que num é divisível por i. Ou seja, encontramos um divisor além de 1 e do próprio num.
print(f'{num} não é primo.'): Se a condição if acima for verdadeira (ou seja, num é divisível por i), o programa já sabe que num não é primo. Então, ele imprime essa mensagem.

break: Assim que um divisor é encontrado, não precisamos mais continuar o loop, porque já sabemos que o número não é primo. O comando break serve para parar o loop imediatamente.

else: (associado ao for): Essa é uma característica um pouco diferente do Python. O else aqui não está ligado ao if de dentro do loop, mas sim ao próprio for.

Este else só será executado se o for terminar naturalmente, ou seja, se o loop rodar por todas as divisões possíveis (de 2 até num - 1) e NÃO encontrar nenhum divisor (o break nunca foi acionado).
Se o loop terminar sem encontrar divisores, significa que o num só é divisível por 1 e por ele mesmo.
print(f'{num} é primo.'): Se o else do for for executado, significa que o número é primo, e essa mensagem é exibida.

Python

else:
    print('Números menores ou iguais a 1 não são primos.')
else: (associado ao primeiro if num > 1:): Se a primeira condição lá em cima (if num > 1:) for falsa, ou seja, se o usuário digitou um número menor ou igual a 1.
print('Números menores ou iguais a 1 não são primos.'): Essa mensagem é exibida, porque, como já dissemos, números primos são sempre maiores que 1 por definição.
Em Resumo
O código pede um número, verifica se ele é maior que 1. Se for, ele tenta dividir esse número por todos os inteiros de 2 até um pouco antes dele. Se ele encontrar qualquer divisor (sem resto), ele diz que o número não é primo e para. Se ele passar por todas as divisões e não encontrar nenhum divisor, aí sim, ele conclui que o número é primo! Simples e eficaz!
    '''