class Vehicle:
    def __init__(self , color , price , type):
        self.color = color
        self.price = price
        self.type = type
    def drive(self):
        print(self.color , self.type , "поехал")
    def brake(self):
        print(self.color , self.type , "остановился")
car1 = Vehicle("белый" , "20000" , "автомобиль")
car2 = Vehicle("красный" , "100000" , "грузовой")

car1.drive()
car1.brake()