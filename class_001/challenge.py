# Inform name, salary and commission, returns commission amount

name = input("Type your name: ")
salary = float(input("Type your salary: "))
commission = float(input("Type your commission (rate): "))

commission_amount = float(1000) + salary * commission

print(commission_amount)

print(f"The user {name} has a commission amount of {commission_amount}.")