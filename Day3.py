#Program 1:
'''
from datetime import date
todays_date=date.today()
def find_age(birth_year):
    age = todays_date.year - birth_year
    print(age)

find_age(1980)
find_age(2015)
'''
 #Program 2:
def calculator(number1,number2):
    addition = number1 + number2
    substraction = number1 - number2
    multiplication = number1 * number2
    floor_division = number1 // number2
    decimal_division = number1 / number2
    remainder = number1 % number2
    power = number1 ** number2
    print("Addition of given two numbers is:{}".format(addition))
    print("Substraction of given two numbers is:{}".format(substraction))
    print("Multiplication of given two numbers is:{}".format(multiplication))
    print("Floor Division of given two numbers is:{}".format(floor_division))
    print("Decimal Devision of given two numbers is:{}".format(decimal_division))
    print("Remainder after division of given two numbers is:{}".format(remainder))
    print("Power of given two numbers is:{}".format(power))

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
print(calculator(number1,number2))
