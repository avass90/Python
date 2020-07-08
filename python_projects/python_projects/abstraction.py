from abc import ABC, abstractmethod
class drink(ABC):
    def drinkOrder(self, flavor):
        print("You ordered a: ", flavor)
    @abstractmethod
    def extras(self, flavor):
        pass

class HowWouldYouLikeIt(drink):
    def extras(self, flavor):
        print("Would you like any cream or sugar in your {}?".format(flavor))

obj = HowWouldYouLikeIt()
obj.drinkOrder("Coffee")
obj.extras("Coffee")
