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
    s1 = int(input('Primeiro segmento: \033[32m'))
    s2 = int(input('\033[mSegundo segmento: \033[32m'))
    s3 = int(input('\033[mTerceiro segmento: \033[32m'))


def main():
    limpa_tela()
    cabecalho()

main()