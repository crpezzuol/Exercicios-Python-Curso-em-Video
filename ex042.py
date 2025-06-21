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
    a = int(input('Primeiro segmento: \033[32m'))
    b = int(input('\033[mSegundo segmento: \033[32m'))
    c = int(input('\033[mTerceiro segmento: \033[32m'))
    print('\n\033[m')
    if a + b > c and a + c > b and b + c > a:
        print('\nThe lengths can form a triangle.\n')
    else:
         print('\nOs segmentos acima \033[1;31mNÃO PODEM\033[m formar um TRIÂNGULO.\n')



def main():
    limpa_tela()
    cabecalho()
    seg_triangulos()

main()