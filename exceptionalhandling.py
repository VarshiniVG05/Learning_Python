#1. Write a Python program that asks the user to input a number and prints the reciprocal of that number. Handle the exception if the user inputs zero
# try:
#     number=int(input("Enter a number"))
#     reciprocal = 1 / number
#     print("Reciprocal is:",reciprocal)
# except ZeroDivisionError:
#     print("error:cannot divide by zero.")
# except ValueError:
#     print("error:please enter a valid number.")

# 2. modify the above program to also handle the exception if the user inputs a non-numeric value

# try:
#     number= float(input("Enter a number: "))
#     reciprocal = 1 / number
#     print("Reciprocal is:",reciprocal)
# except ZeroDivisionError:
#     print("error:cannot divide by zero.")
# except ValueError:
#     print("error:please enter a numeric value.")

# 3. write a program that reads a number from the user and prints its square.use the else clause to print a success message

# try:
#     number=int(input("enter a number:"))
#     square = number**2
#     print("square of the number is:",square)
# except ValueError:
#     print("error:please enter a valid number.")
# else:
#     print("success:square calculated successfully")

# # 4. modify the program in Task 3 to include a finally clause that prints a message regardless of whether an exception occurred or not

# try:
#     number=int(input("Enter a number:"))
#     square = number** 2
#     print("Square of the number is:",square)
# except ValueError:
#     print("error:please enter a valid number.")
# else:
#     print("success:square calculated successfully")
# finally:
#     print("program execution completed.")

# 5. write a function that raises a valueerror if the input number is negative

# def check_positive(number):
#     if number<0:
#         raise ValueError("negative numbers are not allowed.")
#     else:
#         print("number is valid")

# 6. Write a program that repeatedly asks the user for a number and handles exceptions. The program should continue asking until a valid number is entered.

# while True:
#     try:
#         number=int(input("Enter a number:"))
#         print("you entered",number)
#         break 
#     except ValueError:
#         print("invalid input,please enter a valid number")

