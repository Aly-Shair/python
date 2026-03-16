# int(2.23)
# float(40)
# "chai" + "code" # operator overloading

# x = 1
# y = 2
# z = 3
# print(x, y, z) # give tuple in shell
# print(x + 1, y ** 3)
# print(y % 2)
# print(1/3)

# repr("chai")
# print(repr("chai"))
# str("code")
# print(str("code"))

# data = {"name": "John", "score": 9.5}
# print("Log:", str(data))   # Pretty normal
# print("Log:", repr(data))  # Shows raw format


# >>> repr("chai")
# "'chai'"
# >>> str("chai")
# 'chai'
# >>> print("chai")
# chai


# >>> 1 < 2 < 3
# True
# >>> 1 == 2 < 3
# False
# >>> 1 == 2 and 2 < 3
# False
# >>> 

# math.floor gives closest number before value
# math.trunk turns you towards zero
# import math;
# print(math.floor(3.5))
# print(math.floor(-3.5))
# print(math.trunc(-3.5))

# >>> 9999999999999999999999999999999 + 1
# 10000000000000000000000000000000
# >>> 99999999999999999999999999999999 * 2.1
# 2.1e+32 # we can deal this


# handle imaginary numbers in python
# >>> 2+j
# Traceback (most recent call last):
#   File "<python-input-28>", line 1, in <module>
#     2+j
#       ^
# NameError: name 'j' is not defined
# >>> 2+1j
# (2+1j)
# >>> 2+1j*3
# (2+3j)
# >>> (2+1j)*3
# (6+3j)

# octal number 
# octal numbers start with 0o
# >>> 0o20
# 16

# hex numbers
# hex numbers start with 0x
# >>> 0xff
# 255 

# binary literals
# start with 0b
# >>> 0b00000001
# 1
# >>> 0b02
#   File "<python-input-5>", line 1
#     0b02
#        ^
# SyntaxError: invalid digit '2' in binary literal
# >>> 0b1
# 1
# >>> 0b10000000
# 128
# >>> 

# decimal to other base numbers
# >>> oct(64)
# '0o100'
# >>> hex(64)
# '0x40'
# >>> bin(64)
# '0b1000000'
# >>>

# convert other base numbers to int
# >>> int("64", 8)
# 52  
# >>> int('64', 16)
# 100 
# >>> int("10000000", 2)
# 128 
# >>> int("2", 2)
# Traceback (most recent call last):
#   File "<python-input-19>", line 1, in <module>       
#     int("2", 2)
#     ~~~^^^^^^^^
# ValueError: invalid literal for int() with base 2: '2'
# >>> 

#  bitwise operator
# >>> x = 2
# >>> x
# 2
# >>> x << 2
# 8
# >>> x | 1
# 3
# >>> x & 5
# 0
# >>> x | 1
# 3
# >>> x & 3
# 2
# >>> 

# random number generator method
# >>> import random
# >>> random.random()
# 0.7761153032339234
# >>> 
# >>> random.random()
# 0.9866768845737265
# >>> random.randint(1, 2)
# 1   
# >>> random.randint(1, 3)
# 3   
# >>> 

# import random;
# print(random.randint(1, 3));
# l1 = ["lemon", "ginger", "mint"];
# print(random.choice(l1))
# print(l1)
# random.shuffle(l1)
# print(l1)
# random.shuffle(l1)
# print(l1)
# random.shuffle(l1)
# print(l1)
# random.shuffle(l1)
# print(l1)


# decimal problem in python solved
# >>> 0.1 + 0.1 + 0.4
# 0.6000000000000001
# >>> 0.1 + 0.1 + 0.1 - 0.3
# 5.551115123125783e-17
# >>> (0.1 + 0.1 + 0.1) - 0.3
# 5.551115123125783e-17
# >>> from decimal import Decimal
# >>> Decimal("0.1") + Decimal("0.1") + Decimal('0.1')
# Decimal('0.3')
# >>> Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")
# Decimal('0.0')
# >>> 

# fractions in python
# >>> from fractions import Fraction
# >>> myFrac = Fraction(2, 7)
# >>> myFrac
# Fraction(2, 7)
# >>>


# sets in python # & is used for intersection and | is used for union
# >>> setOne = {1, 2, 3, 4}
# >>> setOne & {1, 3, 7}
# {1, 3}
# >>> setOne | {1, 3, 7}
# {1, 2, 3, 4, 7}
# >>> setOne - {1, 2, 3, 4}
# set() # it gives empty set as set() not as {} cuz empty paranthesis are dict
# >>> type({})
# <class 'dict'>
# >>> setTwo = {1, 2, 3, 4, 4, 1}
# >>> setTwo
# {1, 2, 3, 4}
# >>> 

# booleans
# >>> type(True)
# <class 'bool'>
# >>> type(1)
# <class 'int'>
# >>> True == 1
# True
# >>> True is 1
# <python-input-120>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
#   True is 1
# False
# >>> True + 4
# 5   
# >>> True - 5
# -4  
# >>> False - 1
# -1  
# >>> 