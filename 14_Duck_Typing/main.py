class Animal :
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof")
class cat(Animal):
    def speak(self):
        print("meow")

animals =[Dog(),cat()]

for animal in animals:
    animal.speak()