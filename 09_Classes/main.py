class Student :
    school ="ABC school"

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa

    def introduce(self):
        print(f"hey i am {self.name} and my gpa is {self.gpa}")

    @classmethod
    def my_school(cls):
        print(f"school is {cls.school}")
    

student1 = Student("arjun",24)

student1.introduce()
Student.my_school()