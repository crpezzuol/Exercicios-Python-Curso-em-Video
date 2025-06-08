a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
'''
maior = max(a, b, c)
menor = min(a, b, c)
'''

menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

print(f"\nThe smallest number is: {menor}")
print(f"The largest number is: {maior}")