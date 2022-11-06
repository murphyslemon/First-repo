#problem 1
class Elevator:
    def __init__(self):
        self.floor = 0

    def go_to_floor(self, level):
        print(self.floor)
        while 1:
            if self.floor > level:
                self.floor_down()
                print(self.floor)
            elif self.floor < level:
                self.floor_up()
                print(self.floor)
            else:
                break

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor -= 1

e = Elevator()

e.go_to_floor(-3)
e.go_to_floor(0)

#problem 2
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

#problem 3
class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.elevator_list = []
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        for i in range(number_of_elevators):
            self.elevator_list.append(Elevator())

    def run_elevator(self, elevator_number, floor):
        self.elevator_list[elevator_number].go_to_floor(floor)

    def fire_alarm(self):
        for _i in self.elevator_list:
            _i.go_to_floor(self.bottom_floor)

b1 = Building(-3, 10, 2)

b1.run_elevator(1, 4)
print(b1.elevator_list[1].floor)

b1.fire_alarm()
for x in range(len(b1.elevator_list)):
    print(f"Elevator {x+1} is on floor {b1.elevator_list[x].floor}.")
