#Question 1
# 1.1
class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

lexus = vehicle(240, 18)
print(lexus.max_speed, lexus.mileage)        
# 1.2
class Vehicle:
    pass


# Question 2
# 2.1
class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seat_capacity(self, capacity = 50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

# 2.2
print(School_bus.seat_capacity())


# Question 3
# 3.1
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def color(self, color = 'white'):
        return f'Color: {color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}'


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass

Volvo = Bus('School Volvo', 180, 12)
Audi_Q5 = Car('Audi_Q5', 240, 18)
print(Volvo.color())
print(Audi_Q5.color())

# 3.2
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


# Question 4
# 4.1
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in type()
print(type(School_bus))

# 4.2
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in isinstance() function
print(isinstance(School_bus, Vehicle))


