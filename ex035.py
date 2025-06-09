print ('-=' * 18)
print (' ' * 10 + 'Triangle Analyzer')
print ('-=' * 18)
print('\nInput the lengths of the three sides of a triangle:\n')
a = float(input('First side: '))
b = float(input('Second side: '))
c = float(input('Third side: ')) 

if a + b > c and a + c > b and b + c > a:
    print('\nThe lengths can form a triangle.\n')
else:
    print('\nThe lengths cannot form a triangle.\n')
