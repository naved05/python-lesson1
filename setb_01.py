"""

car Millage

"""

def millage(fuel):
    intial_km=100
    final_km=500
    milleage=(final_km-intial_km)/fuel

    return milleage

def fuel_ip():

    fuelip=input("enter the fuel:")

    fuel=int(fuelip)

    return fuel

def main():

    fuel=fuel_ip()

    melleage=millage(fuel)

    print("millage of the vechle is ",melleage)

main()
