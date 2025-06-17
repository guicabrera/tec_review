#Abstract Factory
#=========================================================\
class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()
class AbstractProductA:
    def operation_a(self):
        pass
class AbstractProductB:
    def operation_b(self):
        pass

class director:
    def __init__(self, factory: AbstractFactory):
        self._factory = factory
    def some_operation(self):
        product_a = self._factory.create_product_a()
        product_b = self._factory.create_product_b()
        product_a.operation_a()
        product_b.operation_b()
#=========================================================\


#Rate limiting
#=========================================================
import time
def rate_limited(max_per_second):
    def decorator(func):
        min_interval = 1.0 / max_per_second
        def rate_limited_function(*args, **kwargs):
            if not hasattr(rate_limited_function, "_last_call"):
                rate_limited_function._last_call = 0.0
            elapsed = time.time() - rate_limited_function._last_call
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            rate_limited_function._last_call = time.time()
            return func(*args, **kwargs)
        return rate_limited_function
    return decorator
#=========================================================


#timeout execution
#=========================================================
import signal
def timeout(seconds):
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError("Function call timed out")
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wrapper
    return decorator
#=========================================================

#retry using decorator
#=========================================================
def retry(tries, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying due to: {e}")
                    time.sleep(delay)
            raise Exception("Max retries exceeded")
        return wrapper
    return decorator

#=========================================================

from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    name: str
    age: int


if __name__ == "__main__":
    # This will raise a validation error because name is not a string
    try:
        user = User(name=123, age=30)
        print(user)
    except ValueError as e:
        print(f"Validation error: {e}")
