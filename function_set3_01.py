"""
This program prompt user to give two number , and function will check wheather the
number is 2 digit or 3 digit or print the number as it is !!!!
"""



def perform_check(number):
    
        if (number >=10 and number <=99):
            print("the given",number,"is two digit  number")
        elif (number >=100 and number <=999):
            print("The given", number,"is three digit number")
        else:
            print(number)
       
def get_number():
    number1=input("enter the number:")

    number=int(number1)

    return number


num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)
