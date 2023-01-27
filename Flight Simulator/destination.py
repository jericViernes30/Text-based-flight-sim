import planes

airport_lists = {"Philippines":{"Ninoy aquino international airport":"RPLL", "Mactan-cebu airport":"RPVM", "Clark international airport":"RPLC"}, "South korea":{"Incheon":"RKSI", "Gimpo":"RKSS", "Jeju":"RKPC"}}


def departure_info():
    global departure
    global departure_country
    departure_country = input("\nEnter a country to depart\n> ").capitalize()
    if departure_country in airport_lists:
        departure = input("Enter your departure airport\n> ").capitalize()
        

def arrival_info():
    global arrival_country
    global arrival
    arrival_country = input("\nEnter a country to arrive\n> ").capitalize()
    if arrival_country in airport_lists:
        arrival = input("Enter your arrival airport\n> ").capitalize()

def eft_dist():
    if departure == 'Ninoy aquino international airport' and arrival == 'Jeju':
        print("\nEFTime: 2:59h - Dist 12nm")

def plane_selected():
    if planes.pl_select == 1:
        print("AIRBUS A320--200")

def IATA():
    if departure == 'Ninoy aquino international airport' and arrival == 'Jeju':
        print("MNL\t>>>\t CJU\nNinoy\t   \t Jeju Int'l")


def airport_code():
    dep = (airport_lists[departure_country][departure])
    arr = (airport_lists[arrival_country][arrival])
    if departure in (airport_lists[departure_country]):
        if arrival in (airport_lists[arrival_country]):
            print(dep,'\t   \t',arr)
            IATA()

def airport_name():
    pass

def main():
    departure_info()
    arrival_info()
    eft_dist()
    plane_selected()
    airport_code()
