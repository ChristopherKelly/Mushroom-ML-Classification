
def getOdor():
    #Instruct user to perform actions and enter in results
    print("\n\nSTEP 1:   IDENTIFYING THE ODOR")
    print("Without touching the mushroom, try to smell it and select which of the following odors best applies:")
    print("\t1: Spicy\n\t2: Musty\n\t3: Foul\n\t4: Fishy\n\t5: Creosote\n\t6: Pungent\n\t7: Anise\n\t8: Almond\n\t9: None ")
    option = 0
    while (option == 0):
        option = int(input())
        if option in range(1,10):
            if option >=1 and option <= 6:
                print("The Mushroom is Not Edible, it may be Poisonous!")
                return
            if option ==7 or option == 8:
                print("The Mushroom is Edible")
                return
            if option == 9:
                print("More information is needed")
                getSporePrint()
                return
        else:
            print("Invalid option")
            option = 0

def getSporePrint():
    #Instruct user to perform actions and enter in results
    print("\n\nSTEP 2:   IDENTIFYING THE SPORE PRINT COLOUR")
    print("Leave the mushroom on a flat rigid surface for a time. Which of the folowing colours describes the printed spores?")
    print("\t1: Orange\n\t2: Chocolate\n\t3: Buff\n\t4: Brown\n\t5: Black\n\t6: Yellow\n\t7: White")
    option = 0
    while (option == 0):
        option = int(input())
        if option in range(1, 8):
            if option >=1 and option <= 6:
                print("The Mushroom is Edible")
                return
            elif option ==7:
                print("More information is needed!")
                getGillSize()
                return
        else:
            print("Invalid option")
            option = 0

def getGillSize():
    #Instruct user to perform actions and enter in results
    print("\n\nSTEP 3:   IDENTIFYING THE GILL SIZE")
    print("Looking at the underside of the mushroom head, which of the following describes the size of the gills:")
    print("\t1: Broad\n\t2: Narrow")
    option = 0
    while (option == 0):
        option = int(input())
        if option in range(1, 3):
            if option == 1:
                print("The Mushroom is Edible!")
                return
            elif option == 2:
                print("More information is needed")
                getGillSpacing()
                return
        else:
            print("Invalid option")
            option = 0

def getGillSpacing():
    #Instruct user to perform actions and enter in results
    print("\n\nSTEP 4:   IDENTIFYING THE GILL SPACING")
    print("Looking at the underside of the mushroom head, which of the following describes the spacing between the gills:")
    print("\t1: Close\n\t2: Crowded")
    option = 0
    while (option == 0):
        option = int(input())
        if option in range(1, 3):
            if option == 1:
                print("The Mushroom is Not Edible, it may be Poisonous!")
                return
            elif option == 2:
                print("More information is needed")
                getBruising()
                return
        else:
            print("Invalid option")
            option = 0

def getBruising():
    #Instruct user to perform actions and enter in results
    print("\n\nSTEP 5:   IDENTIFYING THE BRUISE COLOUR")
    print("Pressing a sample of the mushroom into a clean surface, does the mushroom change colour and bruise?:")
    print("\t1: Bruises \n\t2: No Bruises")
    option = 0
    while (option == 0):
        option = int(input())
        if option in range(1, 3):
            if option == 1:
                print("The Mushroom is Not Edible, it may be Poisonous!")
                return
            elif option == 2:
                print("The Mushroom is Edible")
                return
        else:
            print("Invalid option")
            option = 0

def main():
    #Greet User
    print("""
                                                           .-'~~~-.
   _____  _                                              .'o  oOOOo`.
  /  ___|| |                                            :~~~-.oOo   o`.
  \ `--. | |__   _ __  _   _  _   _  _ __ ___            `. \ ~-.  oOOo.
   `--. \| '_ \ | '__|| | | || | | || '_ ` _ \             `.; / ~.  OO:
  /\__/ /| | | || |   | |_| || |_| || | | | | |            .'  ;-- `.o.'
  \____/ |_| |_||_|    \__,_| \__,_||_| |_| |_|           ,'  ; ~~--'~
                                                          ;  ;
    (C) Foraging.inc                _______\|/__________\\;_\\//___\|/________""")

    print("\n\nWelcome to Shruum(tm), the mushroom foraging app.")
    print("A handy tool to see if a mushroom is edible or potentially poisonous.")
    print("Using it's data driven platform, this app can identify potentially poisonous mushrooms by their characteristics")

    #Instruct user to perform actions and enter in results
    getOdor()
    input("\n\nPress Enter to end the program.")

main()








    #Notes section

#Rule Induction Results
"""if odor = none then edible  (86 / 2389)
if bruises = no then poisonous  (2433 / 0)
if odor = anise then edible  (0 / 280)
if odor = foul then poisonous  (234 / 0)
if odor = almond then edible  (0 / 277)
else poisonous  (173 / 0)

correct: 5786 out of 5872 training examples."""