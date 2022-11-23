class Person:
    def __init__(self, student_name, height):
        self.student_name = student_name
        self.height = height

    def __str__(self):
        return f"{self.student_name} who is {self.height}cm tall"


class Classroom:
    def __init__(self, class_name, *persons):
        self.class_name = class_name
        self.persons = persons
        self.total_height = 0
        for person in self.persons:
            self.total_height += person.height

    def __str__(self):
        return f"There are {len(self.persons)} students in the {self.class_name} classroom " \
               f"and their combined height is {self.total_height} cm."


steve = Person("Steve", 200)
john = Person("John", 175)
adam = Person("Adam", 185)
anna = Person("Anna", 155)
lucy = Person("Lucy", 165)

maths = Classroom("maths", steve, john, lucy)
# english = Classroom("english", steve, adam, lucy)
# science = Classroom("science", steve, adam, anna, lucy)
# art = Classroom("art", john, anna)

print(maths)
#print(english)
#print(science)
#print(art)
