# class Student:
#     def __init__(self, name, ID):
#         self.name = name
#         self.ID = ID

#     def show(self):
#         print ('name is', self.name, 'ID', self.ID)

# me = Student('omelete', 2345)
# me.show()

# class Circle:
#     def __init__(self, radius):
#         self.pi = 3.14
#         self.radius = radius
    
#     def area(self):
#         print('area is', self.pi*self.radius**2)
#     def perimeter(self):
#         print('perimeter', 2*self.pi*self.radius)
    
# c = Circle(9)
# c.area()
# c.perimeter()
# print(c.pi)
# print(Circle.pi)

class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class Room:
    def __init__(self):
        self.persons = []

    def add_persons(self, person: Person):
        self.persons.append(person)

    def empty_class(self):
        if len(self.persons) == 0:
            print('empty')
        else:
            print('not empty')

    def printing(self):
        total_height = 0
        for person in self.persons:
            total_height += person.height
        print(len(self.persons))
        print(total_height)

me = Person('frank', '175')
chad = Person('chad', '175')

room = Room()

room.add_persons

print(room.empty_class())