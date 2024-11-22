#Write a program in python to demonstrate implicit and explicit type conversion

# Explicit type conversion
y = int(input("Enter a number: "))  # Converting input to integer
print(type(y))  # Displaying the type of 'y' (Explicit conversion)

# Assigning a value to 'x'
x = 10  # Initial value of 'x'

# Implicit type conversion
x = x / 1.5  # 'x' changes from integer to float due to division
print(x, type(x))  # Displaying the value and type of 'x' after implicit conversion



'''
OUTPUT

Enter a number: 6
<class 'int'>
6.666666666666667 <class 'float'>

'''
   
