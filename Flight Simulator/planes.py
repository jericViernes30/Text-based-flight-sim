def airbus_a320_200():
    print("\n\t\t\t   AIRBUS A320-200")
    print("VR Rotation speed\t\t150kn\tMax passengers\t\t180")
    print("VREF Landing speed\t\t133kn\tMax cargo\t\t9220 kg")
    print("VLO Landing gear speed\t\t235kn")
    print("VS Stall speed\t\t\t136kn\tMax flight time estimated\t11:05 h")

def plane_selection():
    global pl_select
    pl_select = int(input("Select a plane to fly\n1. AIRBUS A320-200\n2. BOMBARDIER CRJ900\n3.SAAB 340B\n> "))

def plane_info():
    if pl_select == 1:
        airbus_a320_200()

def main():
    plane_selection()
    plane_info()