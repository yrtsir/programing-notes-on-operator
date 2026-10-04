# ALL 7 TYPES OF OPERATORS IN PYTHON

# 1. Arithmetic Operators
# +, -, *, /, %, **, //
print(5+3) #8

# / always gives float value
print(5/2) #2.5
# // gives integer value
print(5//2) #2
# - subtracts two values
print(5-2) #3
# * multiplies two values
print(5*2) #10
# % gives remainder
print(5%2) #1
# ** gives power
print(5**2) #25

# 2. Comparison Operators
# ==, !=, <, >, <=, >=
# == checks if two values are equal
print(5==5) #True
# != checks if two values are not equal
print(5!=5) #False
# < checks if the first value is less than the second
print(5<2) #False
# > checks if the first value is greater than the second
print(5>2) #True
# <= checks if the first value is less than or equal to the second
print(5<=2) #False
# >= checks if the first value is greater than or equal to the second
print(5>=2) #True

# 3. Logical Operators
# and, or, not
print(True and False) #False
print(True or False) #True
print(not True) #False
print(6 and 3) #3
print(6 or 3) #6
print(6 and 0) #0
print(6 or 0) #6

# 4. Bitwise Operators
# &, |, ^, ~, <<, >>
# & performs bitwise AND operation
print(5 & 3) #1 
# | performs bitwise OR operation
print(5 | 3) #7
# ^ performs bitwise XOR operation
print(5 ^ 3) #6
# ~ performs bitwise NOT operation
print(~5) #-6
# << performs left shift operation
print(5 << 1) #10
# >> performs right shift operation
print(5 >> 1) #2

# 5. Assignment Operators
# =, +=, -=, *=, /=, %=, **=, //=
# = assigns a value to a variable
x = 5   
print(x) #5 
# += adds a value to a variable
x += 3
print(x) #8
# -= subtracts a value from a variable
x -= 2
print(x) #6

# *= multiplies a variable by a value
x *= 2
print(x) #12
# /= divides a variable by a value
x /= 3
print(x) #4.0
# %= gives the remainder of a variable divided by a value
x %= 3
print(x) #1.0
# **= raises a variable to the power of a value
x **= 2
print(x) #1.0
# //= performs floor division on a variable by a value
x //= 2
print(x) #0.0
# 6. Membership Operators
# in, not in
# in checks if a value is present in a sequence
print(3 in [1, 2, 3, 4, 5]) #True
# not in checks if a value is not present in a sequence 
print(6 not in [1, 2, 3, 4, 5]) #True

# 7. Identity Operators
# is, is not
# is checks if two variables refer to the same object
x = 5
y = 5
print(x is y) #True
# is not checks if two variables do not refer to the same object
print(x is not y) #False