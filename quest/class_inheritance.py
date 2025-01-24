# - class Vehicle(brand, model)
#  + get_info()

# - Car(Vehicle)
#  + get_info() 상속
#  + ride_info(wheels)
# - Truck(Vehicle)
#  + get_info() 자체
#  + more_info(wheels)

class Vehicle(): 
    def __init__(self, brand = 'Benz'):
        self.brand = brand
        pass
    
    def model(self, made_year):
        return f'{made_year} 년도에 만들어졌습니다.'

class Car(Vehicle):
    def __init__(self):
        pass
    
    def get_info(self, made_year):
        return f'{made_year} 년도에 만들어졌습니다.'

    def ride_info(self, wheels):
        return f'{wheels}생산년도 확인' 
        
class Truck(Vehicle):
    def __init__(self):
        pass
    
    def get_info(self, made_year):
        return f'{made_year} 년도에 만들어진 제품은 수리가 적다'
    
    def more_info(self, wheels):
        return f'{wheels} 부분이 제일 튼튼하다.'
    
        
if __name__=='__main__':
    car = Car()
    truck = Truck()
    car.get_info('2025')
    car.ride_info('2024')
    truck.get_info('2020')
    truck.more_info('타이어')