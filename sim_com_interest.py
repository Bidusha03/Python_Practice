# Program to calculate Simple Interest and Compound Interest

# Input principal, rate of interest, and time period from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Calculate Compound Interest
compound_interest = principal * (1 + rate / 100) ** time - principal

# Display the results
print("Simple Interest:", simple_interest)
print("Compound Interest:" ,compound_interest)


'''
OUTPUT

Enter the principal amount: 1000
Enter the annual rate of interest (in %): 5
Enter the time period (in years): 2
Simple Interest: 100.0
Compound Interest: 102.5

'''
