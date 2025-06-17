from abc import abstractmethod, ABC

# Abstract Factory
#-------------------------------------------------------------------------------------------------
class car_parts_factory(ABC):
    @abstractmethod
    def create_body():
        ...    
    @abstractmethod
    def create_wheels():
        ...
    
    @abstractmethod
    def create_engines():
        ...


class car_factory_director():
    def __init__(self, car_factory: car_parts_factory):
        self._car_body = car_factory.create_body()
        self._car_wheels = car_factory.create_wheels()
        self._car_engine = car_factory.create_engines()
#-------------------------------------------------------------------------------------------------
