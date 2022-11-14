#Problem 1

# class Car:
#     def __init__(self, registration_number: str, maximum_speed: int):
#         self.registration_number = registration_number
#         self.maximum_speed = maximum_speed
#         self.current_speed = 0
#         self.distance = 0


# new_car = Car('ABC-123', 142)
# print(new_car.registration_number)
# print(new_car.maximum_speed)

#Problem 1 & 2
# class Car:
#     def __init__(self, registration_number: str, maximum_speed: int):
#         self.registration_number = registration_number
#         self.maximum_speed = maximum_speed
#         self.current_speed = 0
#         self.distance = 0

#     def accelerate(self, change_of_speed):
#         speed = self.current_speed + change_of_speed
#         if speed < self.maximum_speed and speed > 0:
#             self.current_speed += change_of_speed
#         elif speed < 0:
#             self.current_speed = 0
#         if speed > self.maximum_speed:
#             print('Exceeds maximum speed')

#     def __str__(self):
#         return "Current speed is: " + str(self.current_speed)

# new_car = Car('ABC-123', 142)

# print(new_car.registration_number)
# print(new_car.maximum_speed)


# new_car.accelerate(+30)
# print(new_car)
# new_car.accelerate(+70)
# print(new_car)
# new_car.accelerate(+50)
# print(new_car)
# new_car.accelerate(-200)
# print(new_car)

#Problem 1 & 2 & 3
class Car:
    def __init__(self, registration_number, maximum_speed: int):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change_of_speed):
        speed = self.current_speed + change_of_speed
        if speed < self.maximum_speed and speed > 0:
            self.current_speed += change_of_speed
        elif speed < 0:
            self.current_speed = 0
        if speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def __str__(self):
        return "Current speed is: " + str(self.current_speed)

    def drive(self, number_of_hours):
        self.distance += self.current_speed * number_of_hours


new_car = Car('ABC-123', 142)

print(new_car.registration_number)
print(new_car.maximum_speed)


new_car.accelerate(+30)
print(new_car)
new_car.accelerate(+70)
print(new_car)
new_car.accelerate(+50)
print(new_car)
new_car.accelerate(-200)
print(new_car)

new_car.distance = 2000
new_car.accelerate(+60)
new_car.drive(1.5)
print(new_car)
print(f"Travelled distance is: {new_car.distance}")

#Problem 4
import random
from prettytable import PrettyTable

def raced_distance(list_of_cars):
    for car in list_of_cars:
        if car.distance > 10000:
            return True
    return False

def update_accelerate(list_of_cars):
    for car in list_of_cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

def print_status(list_of_cars):
    x = PrettyTable()
    x.field_names = ["Registration Number", "Distance", "Current Speed"]
    for car in list_of_cars:
        x.add_row([car.registration_number, car.distance, car.current_speed])
    print(x.get_string(sortby="Distance", reversesort=True))


final_distance = 10000
list_of_cars = []

for i in range(10):
    list_of_cars.append(Car("ABC-" + str(i+1), random.randint(100, 200)))

h = 0
while True:
    if raced_distance(list_of_cars):
        break
    update_accelerate(list_of_cars)

    h += 1

print_status(list_of_cars)
