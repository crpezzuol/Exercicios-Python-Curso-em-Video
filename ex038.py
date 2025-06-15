# This program compares two numbers input by the user.

print('\033[1;33m-=' * 20)
print('\033[1;33m''-' * 10, 'Number  Comparison', '-' * 10, '\033[m')    
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