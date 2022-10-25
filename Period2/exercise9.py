#Exercise 1

# class Car:
#     def __init__(self, registration_number: str, maximum_speed: int):
#         self.registration_number = registration_number
#         self.maximum_speed = maximum_speed
#         self.current_speed = 0
#         self.distance = 0


# new_car = Car('ABC-123', 142)
# print(new_car.registration_number)
# print(new_car.maximum_speed)

#Exercise2
class Car:
    def __init__(self, registration_number: str, maximum_speed: int):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.distance = 0

        def accelerate(self, change_of_speed):
            speed = self.current_speed + change_of_speed
            if speed < maximum_speed and speed > 0:
                self.current_speed += change_of_speed
            elif speed < 0:
                self.current_speed = 0

new_car = Car('ABC-123', 142)

print(new_car.registration_number)
print(new_car.maximum_speed)
print(new_car.current_speed)

new_car.accelerate(+30)
new_car.accelerate(+70)
new_car.accelerate(+50)
new_car.accelerate(-200)