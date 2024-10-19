class Engine:
    def engine_infor(self):
        return "This is engine class"

class Battery:
    def battery_info(slef):
        return "this is ibattery info"


class Electiric_Class(Engine,Battery):
    pass



example = Electiric_Class()
print(example.engine_infor())
print(example.battery_info())