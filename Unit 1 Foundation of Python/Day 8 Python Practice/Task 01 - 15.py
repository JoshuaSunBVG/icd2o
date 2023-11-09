#Task #01

print("Hello Joshua!")
print()

#Task #02

age = 13
height = 1.68
is_student = True

#Task #03

print(f"Name: Joshua, Age: {age}, Height: {height} meters")
print()

#Task #04

import math

print(f"{math.pi:.3f}")
print()

#Task #05

num1 = 10
num2 = 5

print("The sum is " + str(num1 + num2) + ".")
print("The product is " + str(num1 * num2) + ".")
print()

#Task #06

integer = int(input("Enter an integer: "))
integer_square = integer * integer
print("The square of " + str(integer) + " is " + str(integer_square) + ".")
print()

#Task #07

num3 = float(input("Enter a decimal number: "))
num3 = int(num3)
print(num3)
print()

#Task #08

name_1 = input("What is your name: ") 
age_1 = input("How old are you: ")
print(f"Hello, {name_1}! You are {age_1} years old.")
print()

#Task #09

num4 = float(input("Enter a decimal number: "))
num5 = float(input("Enter a decimal number: "))
avg_1 = (num4 + num5) / 2
print(f"{avg_1:.2f}")
print()

#Task #10

#It is important to choose meaningful variable names so you can easily
#understand what it represents in your code.

#An example would be like age = 13 or age = int(input("How old are you: "))

#Task #11

#f strings can handle integers, floats, and booleans because it formats the string
#for you and you do not have to use + or str("variable name")

num6 = int(input("Enter an integer: "))
print(f"The integer is {num6}.")
print()

num7 = float(input("Enter a float: "))
print(f"The float is {num7}.")
print()

is_weekday = bool(input("Is it a weekday? "))
print(f"{is_weekday}, it is a weekday today.")
print()

#Task #12

#Parentheses are used in math for order of operations

print((6 + 8) / 2)
print(6 + 8 / 2)
print()

#In the first one with parentheses it would be 6 + 8 is 14 and then over 2 is 7
#In the second one without parentheses it would be 8 over 2 is 4 and then add 6 is 10

#Task #13

#Formatted f strings can be used to align different text or for decimals and percents
#when dealing with numbers

name = "Joshua"
print(f"{name:<10}")
print(f"{name:^10}")
print(f"{name:>10}")
print()

#Task #14

