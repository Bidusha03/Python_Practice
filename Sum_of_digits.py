# Program to find the sum of digits of a given number

num = int(input("Enter a number: "))  # Input the number
s = 0  # Initialize sum to 0

# Loop to extract digits and calculate their sum
while num != 0:
    r = num % 10  # Get the last digit
    s = s + r     # Add the digit to the sum
    num = num // 10  # Remove the last digit

# Display the result
print("Sum of the digits is:", s)


'''
Output

Enter a number: 123
Sum of the digits is: 6

'''
