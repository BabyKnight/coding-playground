import functools
import time

# Problem 1
def log_execution(func):


    def inner(*args, **kwargs):
        print("Function started")
        try:
            return func(*args, **kwargs)
        finally:
            print("Function finished")

    return inner

@log_execution
def add(a, b):
    return a + b

# Problem 2

def debug(func):

    @functools.wraps(func)
    def inner(*argc, **kwargs):
        print(f"Function: {func.__name__}")
        print(f"Arguments: {argc}, {kwargs}")

        result =  func(*argc, **kwargs)
        print(f"Return value: {result}")
        return result

    return inner

@debug
def calculate_total(price, quantity):
    """Calculate total price."""
    return price * quantity


# Problem 3

def retry(max_attempts=3):
    if max_attempts <= 0:
        raise ValueError("max attempts must ne positive integer")

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*argc, **kwargs):
            attempt = 0

            while attempt <= max_attempts:
                attempt += 1

                try:
                    return func(*argc, **kwargs)

                except Exception:
                    if attempt == max_attempts:
                        raise

        return wrapper

    return decorator


@retry(max_attempts=3)
def connect_server():
    print("Connecting...")
    raise ConnectionError("Connection failed")

# Problem 4

def measure_time(func):

    @functools.wraps(func)
    def wrapper(*argc, **kwargs):
        start = time.perf_counter()
        try:
            return func(*argc, **kwargs)
        # make it work after return
        finally:
            end = time.perf_counter()
            print(f"{func.__name__} takes {end - start} s")

    return wrapper


@measure_time
def process_packages(packages):
    return [pkg for pkg in packages if pkg["enabled"]]


# Problem 5

def require_role(required_role):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            role = kwargs.get("role")
            if role != required_role:
                raise PermissionError(f"required role: {required_role}")

            return func(*args, **kwargs)

        return wrapper
    return decorator


@require_role("admin")
def delete_package(package_id, role):
    return f"Deleted {package_id}"


import inspect
# Problem 6 
def cache_result(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        key = (args, tuple(sorted(kwargs.items())))
        print(f"Key is -------------{key}")

        if key not in cache:
            print("No cache found, Calculating...")
            cache[key] = func(*args, **kwargs)

        return cache[key]

    cache = {}
    return wrapper

@cache_result
def calculate(a, b):
    print("Calculating...")
    return a + b

# Process 8
class FileManager():
    def __init__(self, filename, mode="r"):
        self._filename = filename
        self._mode = mode
        self._fp = None

    def __enter__(self):
        # execute when using with... open the file
        # return value is the value of 'as' (with ... as Xx)
        self._fp = open(self._filename, self._mode)
        return self._fp
        #return [1, 2, 3]

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._fp is not None:
            self._fp.close()
        return False

# Problem 9

class Timer():

    def __init__(self, msg):
        self.msg = msg
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print(f"{self.msg} took {self.end - self.start} secnods")
        return False





if __name__ == "__main__":
    result = add(10, 20)
    print(result)

    print(calculate_total.__name__)
    print(calculate_total.__doc__)
    print(calculate_total(12, 11))

    try:
        connect_server()
    except Exception:
        pass

    packages = [
        {"name": "firefox", "enabled": True},
        {"name": "vim", "enabled": False},
        {"name": "vlc", "enabled": True},
        {"name": "git", "enabled": True},
    ]
    res = process_packages(packages)
    print(res)

    delete_package("pkg-001", role="admin")
    #delete_package("pkg-001", role="user")

    print(calculate(10, 20))
    print(calculate(10, 20))
    print(calculate(10, 30))
    print(calculate(a=10, b=30))

    def decorator_a(func):
        def wrapper(*args, **kwargs):
            print("A start")
            result = func(*args, **kwargs)
            print("A end")
            return result
        return wrapper


    def decorator_b(func):
        def wrapper(*args, **kwargs):
            print("B start")
            result = func(*args, **kwargs)
            print("B end")
            return result
        return wrapper


    @decorator_a
    @decorator_b
    def process():
        print("Processing...")


    process()

    with FileManager("day7.py", "r") as f:
        print(f)


    def process_packages():
        time.sleep(0.2)
        # raise RuntimeError("something wrong")

    with Timer("Package Processing"):
        process_packages()

