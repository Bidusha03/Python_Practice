# Program to calculate the area of a triangle using Heron's formula

import math

# Input the lengths of the sides of the triangle
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Display the result
print(" The area of the triangle is: ", area)

'''
OUTPUT

Enter the length of the first side: 4
Enter the length of the second side: 5
Enter the length of the third side: 6
The area of the triangle is:  9.921567416492215

'''
