# Class bike used to define further objects
class Bike:
    
    # __init__ sets up class objects with a set of values that are
    # passed as parameters. In this case, the objects pass the 
    # following:
    #
    # @param color (str) The color of the bike
    # @param frame_material (str) The material of the frame
    def __init__(self, color, frame_material):
        self.color = color
        self.frame_material = frame_material
        
    # Brake is a method which prints a simple statement when called
    def brake(self):
        print('Braking!')

# Specific bike objects
red_bike = Bike('Red', 'Carbon Fiber')
blue_bike = Bike('Blue', 'Steel')
green_bike = Bike('Green', 'Magnesium')

# Using objects which are instances of a higher class
print(red_bike.color) # should print 'Red'
print(red_bike.frame_material) # Should print 'Carbon Fiber'
print(green_bike.color) # Should print 'Green'
print(blue_bike.frame_material) # Should print 'Steel'

# Braking using class and objects
red_bike.brake() # Should print 'Braking!'