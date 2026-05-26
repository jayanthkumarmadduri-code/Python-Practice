class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)


    def set_name(self, name):
        if name.strip() == "":
            print("Name cannot be empty")
        else:
            self.__name = name


    def get_name(self):
        return self.__name


    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100")


    def get_roll_no(self):
        return self.__roll_no


    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative")


    def get_marks(self):
        return self.__marks



s1 = Student("Jayanth", 25, 90)

print("Name:", s1.get_name())
print("Roll No:", s1.get_roll_no())
print("Marks:", s1.get_marks())