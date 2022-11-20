# problem 1
# class Elevator:
#     def __init__(self):
#         self.floor = 0
#
#     def go_to_floor(self, level):
#         print(self.floor)
#         while 1:
#             if self.floor > level:
#                 self.floor_down()
#                 print(self.floor)
#             elif self.floor < level:
#                 self.floor_up()
#                 print(self.floor)
#             else:
#                 break
#
#     def floor_up(self):
#         self.floor += 1
#
#     def floor_down(self):
#         self.floor -= 1
#
# e = Elevator()
#
# e.go_to_floor(-3)
# e.go_to_floor(0)

# problem 2
# class Building:
#     def __init__(self, bottom_floor, top_floor, number_of_elevators):
#         self.elevator_list = []
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#         self.number_of_elevators = number_of_elevators
#         for i in range(number_of_elevators):
#             self.elevator_list.append(Elevator())

#     def run_elevator(self, elevator_number, floor):
#         self.elevator_list[elevator_number].go_to_floor(floor)

# b1 = Building(-3, 10, 2)

# b1.run_elevator(1, 4)
# print(b1.elevator_list[1].floor)

# problem 3
# class Building:
#     def __init__(self, bottom_floor, top_floor, number_of_elevators):
#         self.elevator_list = []
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#         self.number_of_elevators = number_of_elevators
#         for i in range(number_of_elevators):
#             self.elevator_list.append(Elevator())
#
#     def run_elevator(self, elevator_number, floor):
#         self.elevator_list[elevator_number].go_to_floor(floor)
#
#     def fire_alarm(self):
#         for y in self.elevator_list:
#             y.go_to_floor(self.bottom_floor)
#
# b1 = Building(-3, 10, 2)
#
# b1.run_elevator(1, 4)
# print(b1.elevator_list[1].floor)
#
# b1.fire_alarm()
# for x in range(len(b1.elevator_list)):
#     print(f"Elevator {x+1} is on floor {b1.elevator_list[x].floor}.")

# problem 4
import random
from prettytable import PrettyTable

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

class Race:
    def __init__(self, race_name, race_distance, car_list):
        self.race_name = race_name
        self.race_distance = race_distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
    
    def race_finished(self):
        for car in self.car_list:
            if car.distance > self.race_distance:
                return True
        return False

    def print_status(self):
        x = PrettyTable()
        x.field_names = ["Registration Number", "Distance", "Current Speed"]
        for car in list_of_cars:
            x.add_row([car.registration_number, car.distance, car.current_speed])
        print(x.get_string(sortby="Distance", reversesort=True))

list_of_cars = []

for i in range(10):
    list_of_cars.append(Car("ABC-" + str(i+1), random.randint(100, 200)))

r1 = Race("Grand Demolition Derby", 8000, list_of_cars)
print(f"{r1.race_name} is {r1.race_distance}kms long.")

print("Starting race")

hour = 0
while not r1.race_finished():
    r1.hour_passes()
    hour += 1

    if hour % 10 == 0:
        print(f"After {hour}hrs")
        r1.print_status()
print(f"final result after {hour}hrs is: ")
r1.print_status()