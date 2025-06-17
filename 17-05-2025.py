#------------------------------------------------------
from abc import ABC, abstractmethod

# Abstract Product
class AbstractProduct(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Product A
class ConcreteProductA(AbstractProduct):
    def operation(self):
        return "Result of ConcreteProductA"

# Concrete Product B
class ConcreteProductB(AbstractProduct):
    def operation(self):
        return "Result of ConcreteProductB"

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self) -> AbstractProduct:
        pass

# Concrete Factory A
class ConcreteFactoryA(AbstractFactory):
    def create_product(self) -> AbstractProduct:
        return ConcreteProductA()

# Concrete Factory B
class ConcreteFactoryB(AbstractFactory):
    def create_product(self) -> AbstractProduct:
        return ConcreteProductB()

# Usage example
def client_code(factory: AbstractFactory):
    product = factory.create_product()
    print(product.operation())

#------------------------------------------------------


#rate limiting decorator factory pattern
#that is the kind of function that will check if the executions in certain time is in the limite per time



if __name__ == "__main__":
    #1
    client_code(ConcreteFactoryA())
    client_code(ConcreteFactoryB())
    #2