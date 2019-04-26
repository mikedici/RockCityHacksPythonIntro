# Python is what is called and "Object Oriented" which means that we organize
# our code into logical chunks called "Classes" these classes are similar
# to blueprints for building a MacDonalds. they describe a MacDonalds 
# but it cant give you any burgers unless you build it.
# The building is called an object.

class McDonalds:
    def __init__(self):
        self.menu = ["Happy Meal", "Qtr Pounder", "Dbl Qtr Pounder", "Big Mac"]
    
    def addMenuItem(self, item):
        self.menu.append(item)
        return

myRestaurant = McDonalds()

print(myRestaurant)
print(myRestaurant.menu)
myRestaurant.addMenuItem("Fries")
print(myRestaurant.menu)

anotherRestaurant = McDonalds()
print(anotherRestaurant)
print(anotherRestaurant.menu)

# Note that myRestaurant and anotherRestaurant are both instances of McDonalds
# But we only added fries to them menu at myRestaurant.
# They are totally separate objects

