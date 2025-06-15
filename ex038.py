# This program compares two numbers input by the user.

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():

    print('\033[1;33m-=' * 20)
    print('\033[1;33m---- Number Comparison Program ----\033[m')
    print('\033[1;33m-=' * 20)
    print('\033[m')

def print_instructions():
    print('\033[1;33mPlease enter two numbers to compare them.\033[m')
    print('\033[1;33mThe program will tell you which number is greater, or if they are equal.\033[m')
    print('\033[m')

def print_footer():
    print('\033[1;33mThank you for using the number comparison program!\033[m')
    print('\033[1;33m-=' * 20)
    print('\033[m')

n1 = float(input("Enter first number: \033[32m"))
n2 = float(input("\033[mEnter second number: \033[32m"))
print('\033[m')

# Compare the two numbers and print the result 

if n1 > n2:
    print(f"The first number \033[34m{n1}\033[m is greater than the second number \033[33m{n2}\033[m")
elif n1 < n2:
    print(f"The second number \033[34m{n2}\033[m is greater than the first number \033[33m{n1}\033[m")
else:
    print(f"The two numbers are equal: \033[34m{n1}\033[m = \033[34m{n2}\033[m")
print('\n')
print("Comparison complete.")
print('\n')

clear_screen()
print_header()  
print_instructions()
print_footer()