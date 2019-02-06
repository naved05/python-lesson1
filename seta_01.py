""" 
Priting the user name 
"""

def get_username():
    
    name=input("enter the user name:")
    return name

def say_hello(user):
    
    print("Hello",user)

def main():
   
    name1 = get_username()
    say_hello(name1)
    
main()
