# Program to check if a number is a perfect number

num = int(input("Enter a number: "))  # Input the number
sum = 0  # Initialize the sum of divisors

# Loop to find divisors and calculate their sum
for i in range(1, num):
    if num % i == 0:  # Check if 'i' is a divisor of 'num'
        sum += i  # Add the divisor to the sum

# Check if the sum of divisors equals the original number
if sum == num:
    print(num,"is a perfect number.")
else:
    print(num,"is not a perfect number.")


'''
OUTPUT

Enter a number: 6
6 is a perfect number.

'''





