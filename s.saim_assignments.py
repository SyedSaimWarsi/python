"""" Declare and initialize two variables, num1 and num2, with integer valuesCalculate and print
their sum."""

num1 = 5
num2 = 10

# Calculate and print their sum
sum = num1 + num2
print("The sum of num1 and num2 is:", sum)

"""Create a variable, message, and assign it a string value. Append another string, " World!", to it
and print the result."""

message = "Hello"

# Append another string to it
message += " World!"

# Print the result
print(message)

"""Define a variable, is_python_fun, and assign it a boolean value. Print a statement based on
whether Python is considered fun."""

is_python_fun = True

# Print a statement based on whether Python is considered fun
if is_python_fun:
    print("Python is considered fun!")
else:
    print("Python is not considered fun.")

    """Create a list, fruits, with three different fruit names. Print the list and then add a new fruit to it.
Print the updated list."""

fruits = ["Apple", "Banana", "Orange"]

# Print the original list
print("Original list of fruits:", fruits)

# Add a new fruit to the list
fruits.append("Grapes")

# Print the updated list
print("Updated list of fruits:", fruits)

"""Declare a variable, price, with a floating-point value. Convert it to an integer and print both the
original and converted values."""

price = 44.4

# Convert it to an integer
price_integer = int(price)

# Print both the original and converted values
print("Original price:", price)
print("Converted price to integer:", price_integer)

"""Create a dictionary, student_info, with keys for 'name', 'age', and 'grade'. Assign corresponding
values and print the dictionary."""

student_info = {
    'name': 'John Doe',
    'age': 18,
    'grade': 'A'
}

# Print the dictionary
print("Student Information:", student_info)

'''Write a program that takes user input for their age and prints a message addressing their age
group (e.g., "Teenager," "Adult")'''

# Take user input for age
user_age = input("Enter your age: ")

# Convert the user input to an integer
age = int(user_age)

# Determine the age group and print a message
if age < 13:
    print("Child")
elif 13 <= age < 20:
    print("Teenager")
elif 20 <= age < 65:
    print("Adult")
else:
    print("Senior Citizen")

'''Define a complex number variable, comp_num, with a real and imaginary part. Print both parts
separately.'''

num = 3 + 4j  # 3 is the real part, 4 is the imaginary part

# Print both parts separately
print("Real part:", num.real)
print("Imaginary part:", num.imag)

'''Combine two strings using string concatenation, and then use string interpolation to include the
length of the resulting string in a print statement.'''

string1 = "Hello"
string2 = "World"

concatenated_string = string1 + string2
concatenated_length = len(concatenated_string)

print(f"The concatenated string is '{concatenated_string}' and its length is {concatenated_length}.")

"""Create a tuple, days_of_week, with the names of the days. Access and print the third day of the
week."""

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Access and print the third day of the week
third_day = days_of_week[2]  # Indexing starts from 0
print("The third day of the week is:", third_day)


