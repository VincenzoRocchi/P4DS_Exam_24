#OBJECT ORIENTED PROGRAMMING
#10/11/2022 lecture(slide 12)

class Engine:
    
    def __init__(self, type):
        self.type = type
        
        
class Vehicle:
    
    def __init__(self, number_of_wheels, type_of_tank, 
                 seating_capacity, maximum_velocity):
        
        self.number_of_wheels = number_of_wheels 
        self.seating_capacity = seating_capacity
        self.type_of_tank = type_of_tank
        self.maximum_velocity = maximum_velocity
        
    def __repr__(self):
        return str({("{},{},{},{}".format(self.number_of_wheels,self.seating_capacity,
                                      self.type_of_tank,self.maximum_velocity))})


Tesla_s = Vehicle(4, "electric", 5, 350)
print(Tesla_s)


#%% ex1

# =============================================================================
# Modify the constructor of last class Vehicle (that refers an Engine object) 
# so that it initialises the number of wheels, seating capacity, and max 
# speed attributes when some of them are not passed as argument when the 
# object is created
# =============================================================================

class Engine:
    
    def __init__(self, type):
        self.type = type
        
        
class Vehicle:
    
    def __init__(self, number_of_wheels= 0, type_of_tank=0, 
                 seating_capacity=0, maximum_velocity=0):
        
        self.number_of_wheels = number_of_wheels 
        self.seating_capacity = seating_capacity
        self.type_of_tank = type_of_tank
        self.maximum_velocity = maximum_velocity
        
    def __repr__(self):
        return str({("{},{},{},{}".format(self.number_of_wheels,self.seating_capacity,
                                      self.type_of_tank,self.maximum_velocity))})


Tesla_s = Vehicle(4, "electric", 5, 350)
print(Tesla_s)

#%% ex2

from math import sqrt, pow

class Point:
    
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    # def __add__(self, other):
    #     return Point(self.x+other.x, self.y+other.y)
    
    # def __str__ (self):
    #     return "("+ str(self.x) + "," + str(self.y) + ")"
    
    def get_x (self):
        self.x
    
    def set_x(self, x = 0):
        self.x = x
        
    def get_y (self):
        self.y
    
    def set_y(self, y = 0):
        self.y = y
        
    def translate(self, dx = 0, dy = 0):
        self.x = dx
        self.y = dy
        
    def distance_from_origin(self):
        return (sqrt(pow(self.x,self.y)))
    
    def distance_from_another(self, x1 , x2):
        
        
p1 = Point(4,5)

p1.translate(3,4)

p1.distance_from_origin()



    
    
        

