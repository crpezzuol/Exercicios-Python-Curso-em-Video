# Triangle Analyzer
# This program checks if three given lengths can form a triangle.

print ('-=' * 18)
print (' ' * 10 + 'Triangle Analyzer')
print ('-=' * 18)
print('\nInput the lengths of the three sides of a triangle:\n')
a = float(input('First side: '))
b = float(input('Second side: '))
c = float(input('Third side: ')) 

# Check if the lengths can form a triangle

if a + b > c and a + c > b and b + c > a:
    print('\nThe lengths can form a triangle.\n')
else:
    print('\nThe lengths cannot form a triangle.\n')
