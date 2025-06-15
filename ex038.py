# This program compares two numbers input by the user.

print('\033[1;33m-=' * 20)
print('\033[1;33m''-' * 10, 'Number  Comparison', '-' * 10, '\033[m')    
print('\033[1;33m-=' * 20)
print('\033[m')
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
if n1 > n2:
    print(f"The first number {n1} is greater than the second number {n2}")
elif n1 < n2:
    print(f"The second number {n2} is greater than the first number {n1}")
else:
    print(f"The two numbers are equal: {n1} = {n2}")
print("Comparison complete.")