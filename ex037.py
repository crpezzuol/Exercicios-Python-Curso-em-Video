
# This script prompts the user to enter an integer and then prints it in different number bases.

num = int(input("Please enter an integer number: \033[32m"))
print('\033[m')
base = int(input('Choose one of the numeric bases for conversion: \033[32m'
              '\n1 - Binary'    
              '\n2 - Octal'
              '\n3 - Hexadecimal\n'
              '\n\033[mYour choice: '))
print('\033[m')
if base == 1:
    print(f'The number \033[32m{num}\033[m in binary is: \033[34m{bin(num)[2:]}\033[m')
elif base == 2:
    print(f'The number \033[32m{num}\033[m in octal is: \033[34m{oct(num)[2:]}\033[m')
elif base == 3:
    print(f'The number \033[32m{num}\033[m in hexadecimal is: \033[34m{hex(num)[2:]}\033[m')
else:
    print('\033[31mInvalid option! Please choose a valid base.\033[m')
print('\n')
