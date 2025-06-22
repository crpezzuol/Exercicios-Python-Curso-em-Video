import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print('''                   \033[1;34m     <>
                      <>  <>
                    <>      <>
                  <>          <>
                <>              <>
              <><><><><><><><><><><>\033[m
           ''')
    print('\n\033[m')

def seg_triangulos():
    global a, b, c
    a = int(input('Primeiro segmento: \033[32m'))
    b = int(input('\033[mSegundo segmento: \033[32m'))
    c = int(input('\033[mTerceiro segmento: \033[32m'))
    print('\n\033[m')
    if a + b > c and a + c > b and b + c > a:
    #    tipo_triangulos(a, b, c)
        if a == b == c:
            print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m formar um TRIÂNGULO \033[1;32mEQUILÁTERO!\033[m\n')
        elif a != b and a != c and b != c:
            print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m formar um TRIÂNGULO \033[1;32mESCALENO!\033[m\n')
        elif a == b or a == c or b == c:
           print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m formar um TRIÂNGULO \033[1;32mISÓSCELES!\033[m\n') 
    else:
         print('Os segmentos acima \033[1;31mNÃO PODEM\033[m formar um TRIÂNGULO.\n')

def tipo_triangulos():
    if a == b and a == c:
        print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m formar um TRIÂNGULO \033[1;32mEQUILÁTERO!\033[m\n')
    elif a != b and a != c and b != c:
        print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m formar um TRIÂNGULO \033[1;32mESCALENO!\033[m\n')
    elif a == b or a == c or b == c:
        print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m formar um TRIÂNGULO \033[1;32mISÓSCELES!\033[m\n') 
def main():
    limpa_tela()
    cabecalho()
    seg_triangulos()

main()