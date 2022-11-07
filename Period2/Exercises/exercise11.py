#problem1
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