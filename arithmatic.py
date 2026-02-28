# Arithmatic Operators
# Addition  2+3
# Subtraction 5-2
# Multiplication   3*4
# Division  10/2    
# Modulus 10%3
# Exponentiation    2**3    
# Floor Division    10//3
# Comparison Operators
# Equal to 5==5
# Not equal to 5!=3
# Greater than 5>3
# Less than 5<10
# Greater than or equal to 5>=5
# Less than or equal to 5<=10
# Logical Operators
# And  True and False
# Or   True or False
# Not  not True
# Assignment Operators
# Assignment  x = 5
# Add and assign  x += 3
# Subtract and assign  x -= 2
# Multiply and assign  x *= 4
# Divide and assign  x /= 2
# Modulus and assign  x %= 3
# Exponentiation and assign  x **= 2
# Floor division and assign  x //= 3

num1 = 3
num2 = 2

print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 > num2)   # True
print(num1 < num2)   # False
print(num1 >= num2)  # True
print(num1 <= num2)  # False



print(round(3.75 ))
print(round(3.75, 1))  # round to 1 decimal place
print(round(3.75, 2))  # round to 2 decimal places 



num1= '100'
num2= '200'
print(num1 + num2)  # Concatenation of strings, output: '100200' // not addition of numbers 

num_add = int(num1) + int(num2)  # Convert strings to integers before addition
print(num_add)  # Output: 300
