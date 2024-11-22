#Write a program in python to calculate a distance between 2 points where x1, y1 and x2, y2 are user input.

import math

# Input the coordinates of the first point
x1, y1 = [int(d) for d in input("Enter the value of x1 and y1: ").split()]

# Input the coordinates of the second point
x2, y2 = [int(d) for d in input("Enter the value of x2 and y2: ").split()]

# Correct formula to calculate the distance between the points
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Print the result
print("The distance between two points:", distance)

'''
Output

Enter the value of x1 and y1: 1 2
Enter the value of x2 and y2: 4 6
The distance between two points: 5.0

'''
