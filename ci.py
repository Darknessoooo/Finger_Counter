class Bird:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("Я птича . Меня зовут" , self.name)
b1= Bird("Евлампий")
b2 = Bird("Жанна")

b1.hello()
b2.hello()