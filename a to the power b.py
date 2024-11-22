# Program to calculate a raised to the power of b using a for loop

# Input the values of a and b
a, b = [int(z) for z in input("Enter the value of a, b: ").split()]

# Initialize the result to 1
p = 1

# Multiply a by itself b times
for i in range(1, b + 1):
    p *= a

# Display the result
print("The value of a^b is:", p)


'''
OUTPUT

Enter the value of a, b: 2 3
The value of a^b is: 8

'''
