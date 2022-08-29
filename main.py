"""
# Phase 1: Write a program that asks your name and then greets you by your name
yourname = input("What is your name? ")
print("Hello, " + yourname + "!")

import math

# Phase 2: Write a program that asks the user for the radius of a circle and the prints out the area of the circle
radius = float(input("Input the radius of circle: "))
area = math.pi * radius**2
print(f"The area of this circle is: {area:.2f}")

# Phase 3: Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.
length = float(input("Input the length of the rectangle: "))
width = float(input("Input the width of the rectangle: "))
perimeter = (length + width) * 2
area = length * width
print(f"The perimeter of this rectangle is: {perimeter:.2f}")
print(f"And the area of this rectangle is: {area:.2f}")
"""
# Phase 4: Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.
num01 = int(input("Input 1st integer number: "))
num02 = int(input("Input 2nd integer number: "))
num03 = int(input("Input 3rd integer number: "))
sum = num01 + num02 + num03
product = num01 * num02 * num03
average = float(sum) / 3
print("The SUM of these numbers is:", sum)
print("The PRODUCT of these numbers is:", product)
print(f"The AVERAGE of these numbers is: {average:.2f}")
