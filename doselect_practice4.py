import time
import functools

def log_execution(func):
    """Decorator to log the execution time of a function."""
    @functools.wraps(func)  # Preserves metadata of the original function
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_execution
def add_nums(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Function call
new_res = add_nums(5, 7)
print(f"Result: {new_res}")