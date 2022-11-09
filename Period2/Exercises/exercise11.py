# problem 1
class Publication():
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"Name: {self.name} \nAuthor: {self.author} \nPage count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"Name: {self.name} \nChief editor: {self.chief_editor}")


m1 = Magazine("Donald Duck", "Aki Hyyppä")
m1.print_information()

b1 = Book("Compartment No. 6", "Rosa Liksom", "192")
b1.print_information()

# problem 2
from exercise10 import Car


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(registration_number, maximum_speed)

#working progress
    # def __str__(self):
    #     return "Electric Car: " + str(self.registration_number) + "\nCurrent speed: " + str(
    #         self.current_speed) + "km/h \nDistance: " + str(self.distance) + "km"


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, fuel_tank_size):
        self.fuel_tank_size = fuel_tank_size
        super().__init__(registration_number, maximum_speed, )


E1 = ElectricCar("ABC-15", 180, 52.5)
G1 = GasolineCar("ACD-123", 162, 32.3)

E1.accelerate(150)
E1.drive(3)

print(f"Electric Car: {E1.registration_number} "
      f"\nCurrent speed: {E1.current_speed}km/h "
      f"\nDistance: {E1.distance}km")

G1.accelerate(120)
G1.drive(3)
print(f"Gasoline Car: {G1.registration_number} "
      f"\nCurrent speed: {G1.current_speed}km/h "
      f"\nDistance: {G1.distance}km")

# E1.__str__()