from Cow_Class import *
from Sheep_Class import *
from Chicken_Class import *

def Display_Menu():
    print("\nWhich animals would you like to raise?")
    print("\n1. Cows\n2. Sheep\n3. Chickens\n")

def Option_Select():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2,3):
                valid_option = True
            else:
                print("That option isn't valid. Please enter a valid option.")
        except ValueError:
            print("That option isn't valid. Please enter a valid option.")

    return choice

def Animal_Create():
    Display_Menu()
    choice = Option_Select()
    if choice == 1:
        new_animal = Cow()
    elif choice == 2:
        new_animal = Sheep()
    elif choice == 3:
        new_animal = Chicken()

    return new_animal

def main():
    myAnimal = Animal_Create()
    Manage(myAnimal)

if __name__ == "__main__":
    main()
