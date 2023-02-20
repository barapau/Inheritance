
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color

#color is the only attribute
#get_color is the only method

class Flower(Plant):
    def __init__(self,color, petals): #instance will need two arguments
        Plant.__init__(self,color) #call init method of the superclass (plant)

        self.__petals = petals

    def get_petals(self):
        return self.__petals

