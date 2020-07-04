class step197:
    def __init__(self):
        self._singleUnderscore="protected"
        self.__doubleUnderscore="Private"

    def getPrivate(self):
        print(self.__doubleUnderscore)

    def setPrivate(self, private):
        self.__doubleUnderscore = private

        

obj = step197()
obj._singleUnderscore = "When we use a single underscore, we are warning other developers to not use this object outside of this class"
print(obj._singleUnderscore)
obj.getPrivate()
obj.setPrivate("When we use two underscores we are denoting a private variable.This ensures that a change is not made unless it is intentional.")
obj.getPrivate()

