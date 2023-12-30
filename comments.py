#CONSTRUCTOR

class Point:
    #constructor
    def __init__(self, x, y): #. The self parameter is a reference to the instance of the class. It must always be the first parameter in any instance method.. The self parameter is a reference to the instance of the class. It must always be the first parameter in any instance method.we can use name instead of self
        self.x=x #intializing the attributes of a class
        self.y=y
    def move(self):
        print("move")

var = Point(10, 20) #we are intializing 10 as X and 20 as Y for that we are using a constructor
#var.x=20    ..... we can also change the value
print(var.x)

'''
a constructor is called automatically when an object is created ,by using init method'''