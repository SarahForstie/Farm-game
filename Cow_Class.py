from Animal_Class import *

class Cow(Animal):
    '''This is a child class of Aniaml'''
    #constructor
    def __init__(self):
        super().__init__(1, 6, 7)
        self._type = "Cow"

    def Grow(self, food, water):
        #Overwrites the grow function
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need:
                self._weight = self._weight + self._growth_rate * 2
                
            elif self._status == "Young" and water > self._water_need:
                self._weight = self.weight + self._growth_rate * 1.75
                
            else:
                self._weight = self._weight + self._growth_rate

        else:
            pass

        self._days_grow = self._days_grow + 1
        
        self._Update()
