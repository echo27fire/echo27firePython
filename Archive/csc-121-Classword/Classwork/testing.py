

class Car: # create the car class
    def __init__(self, color, brand, horsepower, wheelbase, tire_size):
        self.color = color
        self.brand = brand
        self.horsepower = horsepower
        self.wheelbase = wheelbase
        self.tire_size = tire_size

    def start(self):
        print("Car is starting")

    def accelerate(self):
        print("Car is accelerating")

# Creating an object of the Car class
my_car = Car("Blue", "BMW", 300, "113 inches", "225/45R18")


class House:
    def __init__(self, bedrooms, bathrooms, square_footage, address):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_footage = square_footage
        self.address = address

    def lock_doors(self):
        print("Doors locked")

    def turn_on_lights(self):
        print("Lights on")

# Creating an object of the House class
my_house = House(3, 2, 1500, "123 Main St")


class Cat:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    def meow(self):
        print("Meow!")

    def purr(self):
        print("Purr...")

# Creating an object of the Cat class
my_cat = Cat("Siamese", 2, "Cream")


