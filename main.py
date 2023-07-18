i = 0
while i == 0:
    try:
        print("\nEnter the day of the week using numbers from 1 to 7.")
        user_select = int(input("\nMake your selection: "))
        match user_select:
            case 1:
                print("\nThe first day of the week is Sunday.")
            case 2:
                print("\nThe second day of the week is Monday.")
            case 3:
                print("\nThe third day of the week is Tuesday.")
            case 4:
                print("\nThe fourth day of the week is Wednesday.")
            case 5:
                print("\nThe fifth day of the week is Thursday.")
            case 6:
                print("\nThe sixth day of the week is Friday.")
            case 7:
                print("\nThe seventh day of the week is Saturday.")
            case _:
                print("\nIncorrect menu number!")
        print("\nDo you want to continue? [Y]Yes or [N]No.")
        user_select2 = input("\nMake your selection: ")

        if user_select2 == "Y" or user_select2 == "y":
            print("\nok let's continue....")
            i = 0
        elif user_select2 == "N" or user_select2 == "n":
            print("\nGood bay!")
            break
        else:
            print("Y or N")
            i += 1
        while i != 0:
            print("\nDo you want to continue? [Y]Yes or [N]No.")
            user_select2 = input("\nMake your selection: ")
            if user_select2 == "Y" or user_select2 == "y":
                print("\nok let's continue....")
                i = 0
            elif user_select2 == "N" or user_select2 == "n":
                print("\nGood bay!")
                break
            else:
                print("\nY or N")
                i += 1


    except ValueError as error:
        print("\nEnter only integer numbers please!")
        i = 0
