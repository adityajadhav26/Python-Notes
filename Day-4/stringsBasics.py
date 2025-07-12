# 1. Accessing characters like arrays:

name = "Aditya"
print(name[0])     # Output: A
print(name[-1])    # Output: a      # java dont provide nevative indexing

# 2. Looping over characters of string:
for ch in name:
    print(ch)

# 3. Slicing:
print( name[1:4] ) #from index1 to index 3.   output: dit

# 4. Immutability- strings are immutable, members/items can not modified,only can access usin name[index]
## name[0] = 'a'      # error : 'str' object does not support item assignment

# 5. To get the length of a string, use the len() function.
myname = "Aditya"
print(len(myname))   # 6

# use of 'in' ,  'not in" 

str1= 'my name is aditya'
print('name' in str1)   # True
if 'aditya' in str1:
    print("aditya is present in str1")

print("rahul" not in str1) # True
if ("rahul" not in str1):
    print("yes, rahul is not in str1")


