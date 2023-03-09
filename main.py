def test(a, b):
    return a+b


class Car:
    def toyota(self):
        print("lest's go with new car")

my_frist_car = Car()
my_frist_car.toyota()

def privet(name):
    print(f'hello {name}')

def third_function():
    print('Hello world!')
    
class ModernCar(Car):
    def third_func(order):
        print('You bought new car')
        
new_car = ModernCar()
new_car.third_func()

