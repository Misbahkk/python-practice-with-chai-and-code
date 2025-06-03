class CAR:
    total_car = 0

    @staticmethod
    def genral_des():
        return " This is a Car Genral method"
    def __init__(self,brand,model):
    #  now we create a __brnad is private
        self.__brnad = brand
        self.__model = model
        CAR.total_car+=1
        
    def get_brand(self):
        return self.__brnad+" !"

    def write(self):
        print(f"Brand: {self.__brnad}, Model: {self.__model}")

    # now we create a polymorphisim example
    def fule_type(self):
        return "desile, Oil"
    

    @property
    def model_acess(self):
        return self.__model+"!"

class ElectricClass(CAR):
    def __init__(self,battery_saver,brnad,model):
       
        super().__init__(brnad,model)
        self.battery_saver = battery_saver

    def fule_type(self):
        return  "Electric"



electricClass = ElectricClass(30,"change",'toyato')
# print(electricClass.battery_saver)
# print(electricClass.model)
# print(electricClass.__brnad) #This is private attribute we can not acess like this
# #this is for provate class
# print(electricClass.get_brand())
# electricClass.write()

# #this is for polymorphism
# print(electricClass.fule_type())


car_class = CAR("yello","beand")
car_class1 = CAR("yello","beand")
# #This is for decorator
print(car_class.genral_des())
print(CAR.genral_des())

# #This is check for polyorphisim
print(car_class.fule_type())
# #add new method
print(electricClass.write())
car_class.write()
## acess a private attribute
# print(car_class.brnad)

print(CAR.total_car)

# this is for property decorator
car_class.model = "city"
print(car_class.model)
print(car_class.model_acess)

print(isinstance(electricClass,CAR))
print(isinstance(electricClass,ElectricClass))








class Car1:

    def __init__(self,name,titel):
        self.name = name
        self.titel= titel


    def Hello(self):
        return f"Hello {self.name} The {self.titel}"
    

class chiled(Car1):

    def __init__(self, name,titel,extra):
        super().__init__(name,titel)
        self.extra =extra

    def GoodBye(self):
        return f"Good Bye {self.name} you are extra {self.extra}"
    


car1 = Car1("misbah","Student")
chiled1 = chiled("MISBAH","developer","mishi")
print(car1.Hello())
print(chiled1.Hello())
print(chiled1.GoodBye())