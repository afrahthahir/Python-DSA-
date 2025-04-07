import time
from functools import wraps

# ✅ Use *args if you're sure it's only positional.
# ✅ Use *args, **kwargs if you want your decorator to work on any function.
#In our functions in binarySearch.py, we are using only positional arguments, so we can use *args

def timing_decorator(func):
    @wraps(func)  # Preserves metadata of the original function
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the actual function
        end_time = time.time()  # Record end time
        print(f"⏱️ '{func.__name__}' took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper