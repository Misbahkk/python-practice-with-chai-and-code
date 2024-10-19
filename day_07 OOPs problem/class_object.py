class CAR:
    total_car = 0
    def __init__(self,brand,model):
    #  now we create a __brnad is private
        self.__brnad = brand
        self.model = model
        CAR.total_car+=1
        
    def get_brand(self):
        return self.__brnad+" !"

    def write(self):
        print(f"Brand: {self.__brnad}, Model: {self.model}")

    # now we create a polymorphisim example
    def fule_type(self):
        return "desile, Oil"


class ElectricClass(CAR):
    def __init__(self,battery_saver,brnad,model):
       
        super().__init__(brnad,model)
        self.battery_saver = battery_saver

    def fule_type(self):
        return  "Electric"



electricClass = ElectricClass(30,"change",'toyato')
print(electricClass.battery_saver)
print(electricClass.model)
# print(electricClass.__brnad) This is private attribute we can not acess like this
print(electricClass.get_brand())
electricClass.write()

print(electricClass.fule_type())


car_class = CAR("yello","beand")
car_class1 = CAR("yello","beand")
print(car_class.fule_type())
print(electricClass.write())
car_class.write()
# print(car_class.brnad)

print(CAR.total_car)