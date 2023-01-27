import os

def ground_systems():
    def gs_systems():
        choice_gs_sys = int(input("\n1.Ground Power Unit\n2.ACU\n3.Pushback\n4.Back\n> "))
        if choice_gs_sys == 1:
            choice_gpu = int(input("1.ON\n2.OFF\n> "))
            if choice_gpu == 1:
                print("GROUND POWER UNIT: ON")
                ground_systems()
            elif choice_gpu == 2:
                print("GROUND POWER UNIT: OFF")
                ground_systems()
        elif choice_gs_sys == 2:
            choice_acu = int(input("1.ON\n2.OFF\n> "))
            if choice_acu == 1:
                print("ACU: ON")
                ground_systems()
            elif choice_acu == 2:
                print("ACU: OFF")
                ground_systems()
        elif choice_gs_sys == 3:
            print("Request for pushback")
            ground_systems()
        elif choice_gs_sys == 4:
            ground_systems()

    def load():
        gross_weight = 58420
        pax_weight_ave = 50
        cargo_weight_ave = 60
        choice_gs_load = int(input("1.PAX DOOR: CLOSED\n2.CARGO DOOR: CLOSED \n3.Back\n> "))
        if (choice_gs_load == 1):
            total_pax = int(input("PAX DOOR: OPEN\nEnter total passengers\n> "))
            pax_weight_ave *= total_pax
            gross_weight += pax_weight_ave
            print("\nTotal pax weight\t", pax_weight_ave, "\nGROSS WEIGHT(AUW)\t", gross_weight)
            load()
        elif (choice_gs_load == 2):
            total_cargo = int(input("CARGO DOOR: OPEN\nEnter total cargo\n> "))
            cargo_weight_ave *= total_cargo
            gross_weight += cargo_weight_ave
            print("\nTotal cargo weight\t", cargo_weight_ave, "\nGROSS WEIGHT(AUW)\t", gross_weight)
            load()
        elif choice_gs_load == 3:
            ground_systems()

    choice_gs = int(input("\n1.Systems\n2.Load\n3.Back\n> "))
    if choice_gs == 1:
        gs_systems()
    elif choice_gs == 2:
        load()
    elif choice_gs == 3:
        main()

def aircraft_systems():
    def as_systems():
        choice_as_sys = int(input("\n1.Main battery\n2.APU\n3.ICE\n4.Seatbelts\n5.No smoking\n6.Back\n> "))
        if choice_as_sys == 1:
            choice_as_sys_main_battery = int(input("\nMAIN BATTERY:\n1.ON\n2.OFF\n> "))
            if choice_as_sys_main_battery == 1:
                print("MAIN BATTERY: ON")
                as_systems()
            elif choice_as_sys_main_battery ==2:
                print("MAIN BATTERY: OFF")
                as_systems()
        elif choice_as_sys == 2:
            choice_as_sys_APU = int(input("\nAPU:\n1.ON\n2.OFF\n> "))
            if choice_as_sys_APU == 1:
                print("APU: ON")
                as_systems()
            elif choice_as_sys_APU ==2:
                print("APU: OFF")
                as_systems()

        elif choice_as_sys == 3:
            choice_as_sys_ICE = int(input("\nICE:\n1.ON\n2.OFF\n> "))
            if choice_as_sys_ICE == 1:
                print("ICE: ON")
                as_systems()
            elif choice_as_sys_ICE ==2:
                print("ICE: OFF")
                as_systems()

        elif choice_as_sys == 4:
            choice_as_sys_seatbelts = int(input("\nSEATBELTS:\n1.ON\n2.OFF\n> "))
            if choice_as_sys_seatbelts == 1:
                print("ADVISORY: Please fasten your seatbelts during take-off and landing")
                as_systems()
            elif choice_as_sys_seatbelts == 2:
                print("SEATBELTS ADVISORY OFF")
                as_systems()

        elif choice_as_sys == 5:
            choice_as_sys_smoking = int(input("\nNO SMOKING:\n1.ON\n2.OFF\n> "))
            if choice_as_sys_smoking == 1:
                print("ADVISORY: Smoking is not allowed at all times during flight")
                as_systems()
            elif choice_as_sys_smoking ==2:
                print("SMOKING ADVISORY OFF")
                as_systems()

        elif choice_as_sys == 6:
            os.system('cls')
            aircraft_systems()
 
    choice_as = int(input("\n1.Systems\n2.Engines\n3.Lights\n4.Checklist\n5.Back\n> "))
    if choice_as == 1:
        as_systems()
    elif choice_as == 2:
        pass
    elif choice_as == 3:
        pass
    elif choice_as == 4:
        pass
    elif choice_as == 5:
        main()


def main():
    choice_main = int(input("\n1.Ground systems\n2.Aircraft Systems\n> "))
    if choice_main == 1:
        ground_systems()
    elif choice_main == 2:
        aircraft_systems()

main()