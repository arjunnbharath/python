count =0
class Student :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self) :
        print(f"hi i am {self.name} and my age is {self.age}")

    def change_age(self,new_age):
        self.age = new_age

    def next_year_age(self):
     return self.age + 1

    @classmethod
    def get_count(cls):
       return cls.count
    

student1 = Student("Arjun",24)
student2 = Student("Rahul", 25)
student1.change_age(75)

age = student1.next_year_age()
student1.change_age(25)
student1.change_age(0)
student1.change_age(150)
print(Student.get_count)
student1.introduce()
student2.introduce()
print(age)