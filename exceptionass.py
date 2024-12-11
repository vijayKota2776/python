###### Write a program to exhibit these concepts:
try:
    input1=int(input("enter number"))
    input2=(input("enter 2 nd number"))
    div=input1+input2
    print(div)
except TypeError as z:
    print(div)
    print(z)
finally:
    print("this is the block that runes at any case")

#program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    input1=int(input("enter number"))
    input2=int(input("enter 2 nd number"))
    div=input1+input2
    print(div)
except ZeroDivisionError as z:
    print(div)
    print(z)

#program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
user_input = input("Please enter an integer: ")
try:
    integer_value = int(user_input)
    print(f"You entered the integer: {integer_value}")
except ValueError:
    raise ValueError("Invalid input: not a valid integer.")

#WAP that exhibits multiple except blocks along with default block
try:
    numerator = int(input("Enter the numerator (an integer): "))
    denominator = int(input("Enter the denominator (an integer): "))
    result = numerator / denominator
    print(f"The result of division is: {result}")
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#WAP that exhibits except blocks that can catch multiple exceptions.
try:
    number = int(input("Enter an integer: "))
    result = 100 / number
    print(f"The result of division is: {result}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")