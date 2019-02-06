""" 
    Printig multiplication table based on user input
"""

def get_number():
    
    number = input("enter the number for multiplaction table: ")
    number = int(number) # it will treat this as an string 
    return number


def print_mtable(num):
    
    for i in range(1,11):
        print(num,"*",i,"=",num*i)

def main():
    '''
        Main program
    '''
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()
