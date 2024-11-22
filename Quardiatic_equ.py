#Write a program in python to calculate the root of a Quardiatic Equation 

import math

# Input the coefficients of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the nature of the discriminant and calculate roots
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The roots are real and distinct.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    # One real repeated root
    root = -b / (2 * a)
    print("The root is real and repeated.")
    print("Root:", root)
else:
    # Complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    print("The roots are complex.")
    print("Root 1:", real_part, "+", imaginary_part, "i")
    print("Root 2:", real_part, "-", imaginary_part, "i")

'''
OUTPUT

Enter the coefficient a: 1
Enter the coefficient b: -3
Enter the coefficient c: 2
The roots are real and distinct.
Root 1: 2.0
Root 2: 1.0

'''
