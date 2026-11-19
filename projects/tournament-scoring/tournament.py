import time #That will make a delay
def tourni(): #Start of a program
    print("""         Tournament""")
    print("""
=============================================================
      Welcome to college tournamnet scoring system
=============================================================
""")
    time.sleep(1)
    Name=input(" Type your name: ")
    while len(Name)==0:
        print("You did not enter a valid participant name")
        print()
        Name=input("Type your name: ")
    print()
    print('Hello',Name,"! Welcome to the college tournament scoring system. Good Luck!")
    print()
    time.sleep(1)
    print("You will be entering five events which can be academic or sports events")
    print()
    time.sleep(1)
    while True:
        ctg=input("Type name from chosen category sports or academics: ")
        ctg=ctg.lower() #all leters will be lowercase
        if ctg == "sports":
            sports=["Basketball","Football","Tennis","Rugby","Cricket","Archery","Bowling","Boxing"]
            print("""
Enter five events from the following:
Basketball
Football
Tennis
Rugby
Cricket
Archery
Boxing
Bowling
""")
            ee1=input("Enter Event 1:") #input of name of first event
            ee1=ee1.capitalize()
            while ee1 not in sports: #check for event starts
                print("You did not enter a valid sports event from the options.Try again")
                print()
                ee1=input("Enter Event 1: ")
                ee1=ee1.capitalize()
                print() #check for event ends
            ee2=input("Enter Event 2:") #input of name of first event
            ee2=ee2.capitalize()
            while ee2 not in sports: #check for event starts
                print("You did not enter a valid sports event from the options.Try again")
                print()
                ee2=input("Enter Event 2: ")
                ee2=ee2.capitalize()
                print() #check for event ends
            ee3=input("Enter Event 3:") #input of name of first event
            ee3=ee3.capitalize()
            while ee3 not in sports: #check for event starts
                print("You did not enter a valid sports event from the options.Try again")
                print()
                ee3=input("Enter Event 3: ")
                ee3=ee3.capitalize()
                print() #check for event ends
            ee4=input("Enter Event 4:") #input of name of first event
            ee4=ee4.capitalize()
            while ee4 not in sports: #check for event starts
                print("You did not enter a valid sports event from the options.Try again")
                print()
                ee4=input("Enter Event 4: ")
                ee4=ee4.capitalize()
                print() #check for event ends
            ee5=input("Enter Event 5:") #input of name of first event
            ee5=ee5.capitalize()
            while ee5 not in sports: #check for event starts
                print("You did not enter a valid sports event from the options.Try again")
                print()
                ee5=input("Enter Event 5: ")
                ee5=ee5.capitalize()
                print() #check for event ends
            print("Your events have been regeistered. You are competing in: ",ee1,",",ee2,",",ee3,",",ee4,",",ee5,". Good Luck!")
            print()
            time.sleep(1)
            break
        elif ctg=="academics":
            academics=["Chess","Painting","Coding","Reading","Trivia","Riddles","Spelling"]
            print("""Enter five events from the following:
Chess
Painting
Coding
Reading
Trivia
Riddles
Spelling
""")
            print()
            ee1=input("Enter Event 1:") #input of name of first event
            ee1=ee1.capitalize()
            while ee1 not in academics: #check for event starts
                print("You did not enter a valid academic event from the options.Try again")
                print()
                ee1=input("Enter Event 1: ")
                ee1=ee1.capitalize()
                print() #check for event ends
            ee2=input("Enter Event 2:") #input of name of first event
            ee2=ee2.capitalize()
            while ee2 not in academics: #check for event starts
                print("You did not enter a valid academic event from the options.Try again")
                print()
                ee2=input("Enter Event 2: ")
                ee2=ee2.capitalize()
                print() #check for event ends
            ee3=input("Enter Event 3:") #input of name of first event
            ee3=ee3.capitalize()
            while ee3 not in academics: #check for event starts
                print("You did not enter a valid academic event from the options.Try again")
                print()
                ee3=input("Enter Event 3: ")
                ee3=ee3.capitalize()
                print() #check for event ends
            ee4=input("Enter Event 4:") #input of name of first event
            ee4=ee4.capitalize()
            while ee4 not in academics: #check for event starts
                print("You did not enter a valid academic event from the options.Try again")
                print()
                ee4=input("Enter Event 4: ")
                ee4=ee4.capitalize()
                print() #check for event ends
            ee5=input("Enter Event 5:") #input of name of first event
            ee5=ee5.capitalize()
            while ee5 not in academics: #check for event starts
                print("You did not enter a valid academic event from the options.Try again")
                print()
                ee5=input("Enter Event 5: ")
                ee5=ee5.capitalize()
                print() #check for event ends
            print("Your events have been regeistered. You are competing in: ",ee1,",",ee2,",",ee3,",",ee4,",",ee5,". Good Luck!")
            print()
            time.sleep(1)
            break
    print("The maximum points you can get per event is 5 and the lowest is 0")
    print()
    ee1p=int(input("Type in your score in "+ee1+": "))
    while ee1p<0 or ee1p>5: #check for event points starts
        print("The value of points is out of range, try again! Value of points must be between 0 and 5")
        print()
        ee1p=int(input("Type in your score in "+ee1+": "))
    ee2p=int(input("Type in your score in "+ee2+": "))
    while ee2p<0 or ee2p>5: #check for event points starts
        print("The value of points is out of range, try again! Value of points must be between 0 and 5")
        print()
        ee2p=int(input("Type in your score in "+ee2+": "))
    ee3p=int(input("Type in your score in "+ee3+": "))
    while ee3p<0 or ee3p>5: #check for event points starts
        print("The value of points is out of range, try again! Value of points must be between 0 and 5")
        print()
        ee3p=int(input("Type in your score in "+ee3+": "))
    ee4p=int(input("Type in your score in "+ee4+": "))
    while ee4p<0 or ee4p>5: #check for event points starts
        print("The value of points is out of range, try again! Value of points must be between 0 and 5")
        print()
        ee4p=int(input("Type in your score in "+ee4+": "))
    ee5p=int(input("Type in your score in "+ee5+": "))
    while ee5p<0 or ee5p>5: #check for event points starts
        print("The value of points is out of range, try again! Value of points must be between 0 and 5")
        print()
        ee5p=int(input("Type in ypur score in "+ee5+": "))
    total=ee1p+ee2p+ee3p+ee4p+ee5p
    print("Calculating your score")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(0.5)
    print("You get",total,"points for all events!")
    time.sleep(0.5)
    #points system ends
    #scoring system starts
    if total <= 10:
        print("You get BRONZE medal!!!")
    elif total <= 20:
        print("You get SILVER medal!!!")
    else:
        print ("You get GOLD medal!!! Congratulations!!!")

    while True:
        pp=input("Do you want to register new participant? Type Yes or No")
        pp=pp.lower()
        if pp=="yes":
            print()
            tourni()
        elif pp=="no":
            print("Thank you for participating. See you soon!")
            break
        else:
            print()
            print("You didnt write Yes or No.Try again")
tourni()
