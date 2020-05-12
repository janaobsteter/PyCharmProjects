from abc import ABC, abstractmethod

class Animal(ABC):
    #add decorator
    @abstractmethod #makes methods abstract - methods that you MUST implement in the subclass
    def weight(self, weight):
        pass

    #@abstractmethod
    def height(self, height):
        pass

#in the subclass, all the mandatory methods have to be redefined! --> but here they actually do something
#with @abstractmethod you only assure, that the method will be included
class Dog(Animal):
    def __init__(self, colour):
        self.colour = colour
    def printColour(self):
        return(self.colour)
    def weight(self, weight):
        return(weight)
    def height(self, height):
        print(height)

dog = Dog("brown")
dog.height("1.5")

