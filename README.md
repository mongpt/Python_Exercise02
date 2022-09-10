# Python_Exercise02
## 2. Variables and interactive programs

1. Write a program that asks your name and then greets you by your name: Examples:
   - If you enter Viivi as your name, the program will greet you with `Hello, Viivi!`.
   - If you enter Ahmed as your name, the program will greet you with `Hello, Ahmed!`.
 ```python
 yourname = input("What is your name? ")
print("Hello, " + yourname + "!")
```
Output console:
```
What is your name? Mong
Hello, Mong!
```
2. Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
```python
import math
radius = float(input("Input the radius of circle: "))
area = math.pi * radius**2
print(f"The area of this circle is: {area:.2f}")
```
Output console:
```
Input the radius of circle: 10
The area of this circle is: 314.16
```
3. Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of 
the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.
```python
length = float(input("Input the length of the rectangle: "))
width = float(input("Input the width of the rectangle: "))
perimeter = (length + width) * 2
area = length * width
print(f"The perimeter of this rectangle is: {perimeter:.2f}")
print(f"And the area of this rectangle is: {area:.2f}")
```
Output console:
```
Input the length of the rectangle: 10
Input the width of the rectangle: 5
The perimeter of this rectangle is: 30.00
And the area of this rectangle is: 50.00
```
4. Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
```python
num01 = int(input("Input 1st integer number: "))
num02 = int(input("Input 2nd integer number: "))
num03 = int(input("Input 3rd integer number: "))
sum = num01 + num02 + num03
product = num01 * num02 * num03
average = float(sum) / 3
print("The SUM of these numbers is:", sum)
print("The PRODUCT of these numbers is:", product)
print(f"The AVERAGE of these numbers is: {average:.2f}")
```
Output console:
```
Input 1st integer number: 1
Input 2nd integer number: 2
Input 3rd integer number: 3
The SUM of these numbers is: 6
The PRODUCT of these numbers is: 6
The AVERAGE of these numbers is: 2.00
```
5. Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). 
The program converts the input to full kilograms and grams and outputs the result to the user:
   - One talent is 20 pounds.
   - One pound is 32 lots.
   - One lot is 13,3 grams.

Example output:
```monospace
Enter talents:
3

Enter pounds:
9

Enter lots:
13.5

The weight in modern units:
29 kilograms and 545.95 grams.
```
```python
talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))
mass = ((talent * 20 + pound) * 32 + lot) * 13.3
mass_kg = int(mass // 1000)
mass_gr = mass % 1000
print("The weight in modern units:", mass_kg, f"kilograms and {mass_gr:.2f} grams")
```
Output console:
```
Enter talents: 10
Enter pounds: 15
Enter lots: 20
The weight in modern units: 91 kilograms and 770.00 grams
```
6. Write a program that draws two random combinations of numbers for a combination lock:
   - a 3-digit code where each number is between 0 and 9.
   - a 4-digit code where each number is between 1 and 6.
```python
import random
# a 3-digit code where each number is between 0 and 9.
digit01 = str(random.randint(0,9))
digit02 = str(random.randint(0,9))
digit03 = str(random.randint(0,9))
print("A 3-digit code where each number is between 0 and 9: " + digit01 + digit02 + digit03)

# a 4-digit code where each number is between 1 and 6
digit01 = str(random.randint(1,6))
digit02 = str(random.randint(1,6))
digit03 = str(random.randint(1,6))
digit04 = str(random.randint(1,6))
print("A 4-digit code where each number is between 1 and 6: " + digit01 + digit02 + digit03 + digit04)
```
Output console:
```
A 3-digit code where each number is between 0 and 9: 387
A 4-digit code where each number is between 1 and 6: 5111
```
