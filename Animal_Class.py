import random
class Animal():
    '''This is the blueprint for the crops'''

    #constructor
    def __init__(self, growth_rate, food_need, water_need):

        #defining the default attributes
        self._weight = 1
        self._days_grow = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = ""
        self._type = "Generic"
        
    def Needs(self):
        #Returns crop needs that were stored in a dictionary
        return{"Light Need": self._food_need, "Water Need": self._water_need}

    def Report(self):
        #Returns the crops info that were kept in a dictionary
        return{"Type": self._type, "Status": self._status, "Growth": self._weight, "Days Growing": self._days_grow}

    def _Update(self):
        #Updates the status of the crop
        if self._weight > 16:
            self._status = "Old"
        elif self._weight > 11:
            self._status = "Mature"
        elif self._weight > 6:
            self._status = "Young"
        elif self._weight > 0:
            self._status = "Baby"
        else:
            self._status = "Not born"

    def Grow(self, food, water):
        #Grows the crop then calls upon _Update in order to change the crop's status
        if food >= self._food_need and water >= self._water_need:
            self._weight = self._weight + self._growth_rate

        self._days_grow = self._days_grow + 1

        self._Update()

def Auto(animal, days):
    #This automatically grows the crop
    for day in range(days):
        food = random.randint(1, 10)
        water = random.randint(1, 10)
        animal.Grow(food,water)

def Manual(animal):
    #This Manually grows the crop using user input
    valid = False
    while not valid:
        try:
            food = int(input("Enter food weight(1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("\nValue not valid. Please enter your value again.\n")
        except ValueError:
            print("\nValue not valid. Please enter your value again.\n")
    valid = False
    while not valid:
        try:
            water = int(input("Enter water value(1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("\nValue not valid. Please enter your value again.\n")
        except ValueError:
            print("\nValue not valid. Please enter your value again.\n")
    animal.Grow(food, water)

def menuDisplay():
    print("\nThis is the Animal managing program.")
    print("\nOptions:")
    print("1. Grow Animal Manually for 1 day")
    print("2. Grow Animal Automatically for 30 days")
    print("3. Report growth status")
    print("4. Exit the program\n")

def menuChoice():
    option = False
    while not option:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option = True
            else:
                print("Option not valid. Please enter your option again.")
        except ValueError:
            print("Option not valid. Please enter your option again.")
    return choice

def Manage(animal):
    noexit = True
    while noexit:
        menuDisplay()
        option = menuChoice()
        print()
        if option == 1:
            Manual(animal)
            print()
        elif option == 2:
            Auto(animal, 30)
            print()
        elif option == 3:
            print(animal.Report())
            print()
        else:
            noexit = False
            print("Thank you for using the animal managing system.")
