"""Chemical plant has a tank for storing ethanol.
            - When the tank is more than 80% full, it
                 should raise an alarm to close the valve.
            - When the tank is less than 20% full, it
                 should send an SMS to buy more liquid.
            - The total tank capacity is 900 litres.
            - Write a program to simulate this.
            - Ask user to enter current level of ethanol in the tank.
            - Print the appropriate action based on value entered
            - Make sure that your program needs minimum changes
                 for a tank of different capacity.
                 """




def get_current_level():
    tank_level=int(input("enter the tank level:"))

    return tank_level

def check_level(level,high,low):

    if (level >=high):

        raise_alarm()

    elif (level <=low):

        send_sms()

    else:
        print("the level of the tank is",level)

def raise_alarm():

    print("please close the valve")

def send_sms():

    print("buy some fuel")
    

# Main starts from here
capacity = 900
high = ((80/100)*capacity)
low = ((20/100)*capacity)
level = get_current_level()
check_level(level, high, low)
