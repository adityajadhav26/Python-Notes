## int can be any positive, naegative, zero number 
x =1
y = 234567889999999999 # unlimited digits
z= -23455
m= 0        # zero is also 'int'

print(type(x))      # int
print(type(y))      # int
print(type(z))      # int
print(type(m))

## float can be any positive, negative, zero with decimal point is must necessity.

x =1.0
y = 23.4567889999999999 # unlimited digits
z= -23.455
m= 0.000       # now zero.zero is 'float

print(type(x))      # float
print(type(y))      # float
print(type(z))      # float
print(type(m))

## note  e denotes poewer of 10, value with e is float 
x = 35e3    #35 into 10^3 is float -> 35 into 1000 = 35000.0
y = 12E4    #120000.0
z = -87.7e100 # -87.7 into 10 to power 100 is float

print(type(x))
print(type(y))
print(type(z))

## type conversion

a = float (15) # 15.0       #int to float
b =  int(-245.345) # -245   # float to int
z = int("3") # z will be 3      #str to int
y= float("45.56")       # str to float
print(a)
print(b)

print(z)
print(y)

print("good bye")