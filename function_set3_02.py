"""Ask the user to enter a number.
            - If the number is a single digit number,
                 add 7 to it, and print the number in its unit’s place
            - If the number is a two digit number,
                raise the number to the power of 5, 
                and print the number in its unit’s place
            - If the number is a three digit number, 
                ask the user to enter another number. 
                Add the 2 numbers and print the number in its unit’s place
            Use the solution provided in S03Q01 as the template for this exercises.
            - Instead of doing a print to print the final result in "perform_check" function 
            call separate functions : 
               do_1digit_oper() and
               do_2digit_oper() and
               do_3digit_oper()
            that will perform the required operations based on the number of digits
            .
            """

def do_1digit_oper(number):
     print("The given", number,"is one digit number")
     act_number=number%10
     print("the given",number,"in its unit place is ",act_number)

def do_2digit_oper(number):

    print("The given", number,"is two digit number")

    pow_num=number**5

    unit_num=pow_num%10

    print("the power of 5 given number is",pow_num,"in its unit place is ",unit_num)


def do_3digit_oper(number1,number2):
    
    print("The given", number1,"is three digit number")

    add_num=number1+number2

    unit_num=add_num%10

    print("the additon of two number is",add_num,"in its unit place is ",unit_num)

     
               
            
def perform_check(number):
    
        if (number >=1 and number <=9):
            do_1digit_oper(number)
            
        elif(number >=10 and number <=99):

            do_2digit_oper(number)
            
        elif (number >=100 and number <=999):
            
            do_3digit_oper(number,get_number())
        else:
            print(number)
       
def get_number():
    number1=input("enter the number:")

    num3=int(number1)

    return num3


num1 = get_number()

perform_check(num1)
