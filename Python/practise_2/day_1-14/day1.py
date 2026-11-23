import copy

def normalize_value(value):
    """
    Normalize input values.

    Rules:
    1. None -> None
    2. String -> strip whitespace
    3. Empty string -> None
    4. Integer / Float -> return unchanged
    5. Boolean -> return unchanged
    6. Other types -> raise TypeError
    """
    if not value:
        return None

    if isinstance(value, str):
        return value.strip()

    if isinstance(value, (int, float, bool)):
        return value

    raise TypeError("Unsupported value type")


#def add_item(item, items=[]): <------ bug!
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


def clone_config(config, deep=False):
    """
    Clone a nested configuration dictionary.

    deep=False: shallow copy
    deep=True: deep copy
    """
    if deep:
        return copy.deepcopy(config)
    else:
        return config.copy()



def create_user(username, *roles, active=True, **metadata):
    """
    Create a user dictionary.

    Example:
    create_user(
        "vincent",
        "admin",
        "developer",
        active=True,
        department="engineering",
        location="Shanghai"
    )
    """
    if username is None:
        return ValueError("username cannot be empty")
    pass


def safe_divide(a, b):
    """
    Return a / b.

    Handle:
    - ZeroDivisionError
    - TypeError
    - ValueError
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        print("Division successful")
        return result
    finally:
        print("Function completed")
