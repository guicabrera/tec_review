import time
from functools import wraps
from collections import deque
import threading

def rate_limit(max_calls, time_window):
    """
    A decorator factory that limits the number of calls to a function within a time window.
    
    Args:
        max_calls (int): Maximum number of calls allowed within the time window
        time_window (float): Time window in seconds
        
    Returns:
        decorator: A decorator that limits the rate of calls to the decorated function
    """
    def decorator(func):
        # Thread-safe call history
        calls = deque()
        lock = threading.RLock()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                # Current time
                now = time.time()
                
                # Remove calls older than the time window
                while calls and calls[0] < now - time_window:
                    calls.popleft()
                
                # Check if we've reached the rate limit
                if len(calls) >= max_calls:
                    wait_time = calls[0] + time_window - now
                    if wait_time > 0:
                        print(f"Rate limit reached. Waiting {wait_time:.2f} seconds...")
                        time.sleep(wait_time)
                        # Refresh the current time
                        now = time.time()
                # Add the current call time
                calls.append(now)
                # Call the original function
                return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage:
# @rate_limit(max_calls=5, time_window=10)
# def my_function():
#     print("Function called!")