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
#             print('exceeds maximum speed')

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
    def __init__(self, registration_number: str, maximum_speed: int):
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
            print('exceeds maximum speed')

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
print(new_car.distance)

#Problem 4
travelled_distance = 0