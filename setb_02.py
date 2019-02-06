"""

Refuleing needed

"""


def fuel_ip():

    fuelip=input("enter the fuel tank capcity:")

    fuel=int(fuelip)

    return fuel

def refilling_req(fuel,distance):

    refilling=distance/fuel
    
    print("number of time refulling required is :",refilling)

def distance_par():

    distance1=input("enter the diatance of place :")

    distance=int(distance1)

    return distance

def main():

    fuel=fuel_ip()

    distance=distance_par()


    refilling=refilling_req(fuel,distance)

main()

    
