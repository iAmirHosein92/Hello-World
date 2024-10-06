patron = input("Patron? (none,some,full) : ")
if patron == "none" :
    print("\033[1;31;1m NO")
elif patron == "some" :
    print("\033[1;32;1m YES")
elif patron == "full" :
    wait_estimate = float(input("Wait Estimate? : "))
    if wait_estimate > 60 :
        print("\033[1;31;1m NO")
    elif 30 < wait_estimate <= 60 :
        alternate = input("Alternate? (yes,no) : ")
        if alternate == "no" :
            reservation = input("Reservation? (yes,no) : ")
            if reservation == "no" :
                bar = input("Bar? (yes,no) : ")
                if bar == "no" :
                    print ("\033[1;31;1m NO")
                if bar == "yes" :
                    print("\033[1;32;1m YES")
            if reservation == "yes" :
                print("\033[1;32;1m YES")
        if alternate == "yes" :
            fri_sat = input("Friday OR Saturday ? (yes,no) : ")
            if fri_sat == "yes" :
                print("\033[1;32;1m YES")
            if fri_sat == "no" :
                print("\033[1;31;1m NO")
    elif  10 < wait_estimate <= 30 :
        hungry = input("Hungry ? (yes,no) : ")
        if hungry == "no" :
            print("\033[1;32;1m YES")
        if hungry == "yes" :
            alternate_2 = input("Alternate ? (yes,no) : ")
            if alternate_2 == "no" :
                print("\033[1;32;1m YES")
            if alternate_2 == "yes" :
                raining = input ("Raining ? (yes,no) : ")
                if raining == "no" :
                    print("\033[1;31;1m NO")
                if raining == "yes" :
                    print("\033[1;32;1m YES")
    elif 0 < wait_estimate <= 10 :
        print("\033[1;32;1m YES")