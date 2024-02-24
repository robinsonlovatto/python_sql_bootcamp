# type 2 whole numbers and prints the division quotient of the first number divided by the second
print("Calculate the division quocient")

# try:
#     number_01 = int(input("Type the first number: "))
#     number_02 = int(input("Type the second number: "))

#     result = number_01 // number_02

#     print(result)
# except ZeroDivisionError:
#     print("integer division or modulo by zero")
# except KeyboardInterrupt:
#     print("You might type something accidentally")


# calculate the area of ​​a circle
# print("Calculate the radius of a circle")
# import math

# radius = float(input("type the radius: "))
# area = math.pi * radius ** 2

# print(f"{area:.2f}")

# Extract date elements from a string in date format
# user_date = input("Type a date in the format dd/mm/yyyy: ")
# list_day_month_year = user_date.split("/")

# print(list_day_month_year)
# print(f"First element = {list_day_month_year[0]}")
# print(f"Second element = {list_day_month_year[1]}")
# print(f"Third element = {list_day_month_year[2]}")
    
# example with TypeError
# try:
    
#     result = len(3)

#     print(result)
# except TypeError as e:
#     print(e)
# else:
#     print("Run if no error occurred in the try block.")
# finally:
#     print("Run no matter what, if error or not.")

print("isinstance example")

number = input("Type an integer number: ")
if isinstance(number, int):
    print("The variable is integer.")
else:
    print("The variable is not integer. Maybe the developer forgot a int() cast enclosing the input()")