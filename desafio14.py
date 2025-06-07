# Peça para o usuário digitar uma frase e informe se ela é um palíndromo (lê-se igual de trás para frente, desconsiderando espaços)
frase = input('Digite uma frase: ').replace(' ', '').lower()
if frase == frase[::-1]:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')
'''
Entendendo o Verificador de Palíndromos
Este código Python tem uma função bem legal: ele verifica se uma frase digitada é um palíndromo. Um palíndromo é uma palavra, frase ou sequência que se lê da mesma forma de trás para frente e de frente para trás, ignorando espaços e letras maiúsculas/minúsculas.

Vamos ver cada parte:

Python

frase = input('Digite uma frase: ').replace(' ', '').lower()
input('Digite uma frase: '): Esta parte exibe a mensagem "Digite uma frase:" para o usuário e espera que ele digite algo e pressione Enter. O que o usuário digitar será armazenado como uma string (texto).
.replace(' ', ''): Este é um método de string que localiza todas as ocorrências de um espaço (' ') na frase digitada e as substitui por uma string vazia (''). Em termos mais simples, ele remove todos os espaços da frase.
.lower(): Este é outro método de string que converte todos os caracteres da frase para minúsculas. Isso é importante para que a capitalização não afete a verificação (por exemplo, "Ovo" e "ovo" sejam tratados da mesma forma).
frase = ...: O resultado dessas operações (a frase sem espaços e em minúsculas) é então guardado na variável frase.
Python

if frase == frase[::-1]:
frase[::-1]: Isso é um truque de Python chamado fatiamento (slicing) que cria uma versão invertida da string frase.
O [:] significa "pegar a string inteira".
O [::-1] especifica um "passo" de -1, que instrui o Python a percorrer a string de trás para frente, efetivamente invertendo-a.
if frase == frase[::-1]:: Esta linha compara a frase original (já limpa) com sua versão invertida.
Se elas forem iguais, significa que a frase se lê da mesma forma de frente para trás e de trás para frente, ou seja, é um palíndromo.
'''