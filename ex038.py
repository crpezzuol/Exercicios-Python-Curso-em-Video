# This program compares two numbers input by the user.

# This program compares two numbers input by the user.
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# This function prints a header message to introduce the program.
def print_header():
    print('\033[1;33m-=' * 36)
    print('\033[1;33m-' * 23,'Number Comparison Program', 22 * '-')
    print('\033[1;33m-=' * 36)
    print('\033[m')

# This function prints instructions for the user on how to use the program.
def print_instructions():
    print('\033[1;33mPlease enter two numbers to compare them.\033[m')
    print('\033[1;33mThe program will tell you which number is greater, or if they are equal.\033[m')
    print('\033[m')

# Prompt the user to enter two numbers
def prompt_user(): 
    n1 = float(input("Enter first number: \033[32m"))
    n2 = float(input("\033[mEnter second number: \033[32m"))
    print('\033[m')

# Compare the two numbers and print the result 
def compare_numbers(n1, n2):
    if n1 > n2:
        print(f"The first number \033[34m{n1}\033[m is greater than the second number \033[33m{n2}\033[m")
    elif n1 < n2:
        print(f"The second number \033[34m{n2}\033[m is greater than the first number \033[33m{n1}\033[m")
    else:
        print(f"The two numbers are equal: \033[34m{n1}\033[m = \033[34m{n2}\033[m")
    print('\n')

# This function prints a footer message to thank the user for using the program.
def print_footer():
    print('\033[1;33m-=' * 36)
    print('\033[1;33mThank you for using the number comparison program!\033[m')
    print('\033[1;33m-=' * 36)
    print('\033[m')

# Main program execution
def main(): 
    clear_screen()
    print_header()
    print_instructions()
    #prompt_user()
    #compare_numbers(n1, n2)
    print_footer()

main()
