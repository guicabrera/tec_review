#Abstract Factory
#-------------------------------------------------
class abstract_car_factory():
    def create_suv(self):
        pass

    def create_sedan(self):
        pass


class honda_factory(abstract_car_factory):
    def create_suv(self):
        return honda_suv()

    def create_sedan(self):
        return honda_sedan()

class toyota_factory(abstract_car_factory):
    def create_suv(self):
        return toyota_suv()

    def create_sedan(self):
        return toyota_sedan()

class abstract_suv():
    def drive(self):
        pass

class abstract_sedan():
    def drive(self):
        pass    

class honda_suv(abstract_suv): 
    def drive(self):
        return "Driving a Honda SUV"

class honda_sedan(abstract_sedan):
    def drive(self):
        return "Driving a Honda Sedan"

class toyota_suv(abstract_suv):
    def drive(self):
        return "Driving a Toyota SUV"

class toyota_sedan(abstract_sedan): 
    def drive(self):
        return "Driving a Toyota Sedan"

class director:
    def __init__(self, factory: abstract_car_factory):
        self._factory = factory

    def some_operation(self):
        suv = self._factory.create_suv()
        sedan = self._factory.create_sedan()
        return suv.drive(), sedan.drive()

if __name__ == "__main__":
    honda = honda_factory()
    toyota = toyota_factory()

    director_honda = director(honda)
    director_toyota = director(toyota)

    print(director_honda.some_operation())
    print(director_toyota.some_operation())
#-------------------------------------------------


#How to use Caching Results with decorator factory?
#-------------------------------------------------

def cache(func):
    cache_data = {}
    def decorator(func):
        def wrapper(*args, **kwargs):
            if args not in cache_data:
                cache_data[args] = func(*args, **kwargs)
            return cache_data[args]
        return wrapper