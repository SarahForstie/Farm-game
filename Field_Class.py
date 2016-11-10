from Carrot_Class import *
from Potato_Class import *
from Wheat_Class import *
from Chicken_Class import *
from Cow_Class import *
from Sheep_Class import *
import random

class Field:
    def __init__(self,max_a,max_c):
        self._crops = []
        self._animals = []
        self._max_a = max_a
        self._max_c = max_c

    def plant(self, crop):
        if len(self._crops) < self._max_c:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self, animal):
        if len(self._animals) < self._max_a:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest(self,position):
        return self._crops.pop(position)

    def remove(self,position):
        return self._animals.pop(position)

    def report_contents(self):
        crop_report = []
        animal_report =[]
        for crop in self._crops:
            crop_report.append(crop.Report())
        for animal in self._animals:
            animal_report.append(animal.Report())
        return{"Crops": crop_report, "Animals", animal_report}

    def report_needs(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.Needs()
            if needs["Light Need"] > light:
                light = needs["Light Need"]
            if needs["Water Need"] > water:
                water = needs["Water Need"]
        for animal in self._animals:
            needs = animal.Needs()
            food = food + needs["Food Need"]
            if needs["Water Need"] > water:
                water = needs["Water Need"]
        return {"Food":food, "Light":light, "Water":water}

    def grow(self,light,food,water):
        if len(self._crops) > 0:
            for crop in self._crops:
                crop.Grow(light,water)
        if len(self._animals) > 0:
            food_needed = 0
            for animal in self._animals:
                needs = animals.Needs()
                food_needed = food_needed + needs["Food Need"]
            if food > food_needed:
                addit_food = food - food_needed
                food = food_needed
            else:
                addit_food = 0
            for animal in self._animals:
                needs = animal.Needs()
                if food >= needs["Food Need"]:
                    food = food - needs["Food Need"]
                    feed = needs["Food Need"]
                    if addit_food > 0:
                        addit_food = addit_food - 1
                        feed = feed + 1
                animal.Grow(feed,water)

def manual_grow(field):
    valid = False
    while not valid:
        try:
            light = int(input("please enter the light value(1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value not valid. Please enter your value again")
        except ValueError:
            print("Value not valid. Please enter your value again")
    valid = False
    while not valid:
        try:
            water = int(input("please enter the light value(1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value not valid. Please enter your value again")
        except ValueError:
            print("Value not valid. Please enter your value again")
    valid = False
    while not valid:
        try:
            food = int(input("please enter the light value(1-10): "))
            if 1 <= food <= 100:
                valid = True
            else:
                print("Value not valid. Please enter your value again")
        except ValueError:
            print("Value not valid. Please enter your value again")

    field.grow(light,food,water)

def auto_grow(field,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        field.grow(light,food,water)

def display_crops(crop_list):
    print("\nCrops in the feild:")
    pos = 1
    for crop in crop_list:
        print("In position", pos,":",crop.Report())
        pos = pos + 1

def display_animals(animal_list):
    print("\nAnimals in the feild:")
    pos = 1
    for animal in animal_list:
        print("In position", pos,":",animal.Report())
        pos = pos + 1

def select_crop(length):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range(1, length+1):
            valid = True
        else:
            print("Please enter a valid option.")
    return selected - 1

def select_animal(length):
    valid = False
    while not valid:
        selected = int(input("Please select an animal: "))
        if selected in range(1, length+1):
            valid = True
        else:
            print("Please enter a valid option.")
    return selected - 1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.remove(selected_animal)

def display_crop_menu():
    print("\nWhich crop type would you like to add?\n")
    print("1. Potato\n2. Wheat\n3. Carrot\n\n0. Return to the main menu\n")

def display_animal_menu():
    print("\nWhich animal type would you like to add?\n")
    print("1. Cow\n2. Sheep\n3. Chicken\n\n0. Return to the main menu\n")

def display_main_menu():
    print("\nThis is the main menu\nPlease choos from the options below\n")
    print("1. Plant a new crop\n2. Harvest a crop\n")
    print("3. Add an animal\n4. Remove an animal\n")
    print("5. Grow field manually over 1 day\n6. Grow field automatically over 30 days\n")
    print("7. Report field status\n\n8. Exit program\n")
#14.27
    
