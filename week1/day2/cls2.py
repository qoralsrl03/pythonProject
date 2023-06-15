#상속
class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print('move')
    def speak(self):
        pass

class Dog(Animal): # animal 상속받음
    #오버라이딩
    def __init__(selfself,nm):
        super().__init__(nm)
        print('animal'+nm)
    def speak(self):
        print('bark')
class Duck(Animal):
    def speak(self):
        print('quack')

dog = Dog('doggy')
print(dog.name)
dog.speak() #오버라이딩한 speak
dog.move() #부모의 move
duck = Duck('donald')
duck.speak()
