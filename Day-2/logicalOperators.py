# higheset precedence  to lowest  : not, and, or

a = True

print(not a)     # False

# and - returns the first falsy value it encounters, or the last value if all are truthy values .
print(( True and 0 and "" and True) ) # 0
print( ("" and 0 and True and True))  # ""

print((True and True and 100))    # 100

# or - returns the first truthy value it finds, or the last falsy value if none are truthy values.
print( (True or 0 or "" or True))  # True
print( ("" or 0 or 100 or True))  # 100

print((False or 0 or ""))    # "" empty string