'''
Both comparison and logical operators are heavily used in both if/else blocks and loops. The logical operators help combine multiple comparisons, while comparison operators do the actual condition checks.
'''

x = 12
y = 9

print(x == y)   # False
# returns False because 12 is not equal to 9

print( x != y )     # True
print(x > y ) # True

if x>y and x!=y :
    # this block exexutes
    print('x is greter than y')
    print('x is not equal to y')
else:
    print('x is smaller than y')

x = 8
y =14

if x>y and x!=y :
    print('x is greter than y')
    print('x is not equal to y')
else:
    # now, this block exexutes
    print('x is smaller than y')


print("out of if else")


if x and y:
    print("both x, y are truthy values, so block will executes")

x = 8
y = 0 

if x and y: 
    print("this will not executes")
else:
    print("else get executes")

print("good bye'")