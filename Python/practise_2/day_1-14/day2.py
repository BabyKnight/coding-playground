import json
from collections import defaultdict

def remove_duplicates(items: list) -> list:
    """
    set(items) is not allowed
    """
    # can deal with dict in list
    result = []

    for x in items:
        # look up in list is O(n)
        if x not in result:
            result.append(x)

    return result


def remove_duplicates_v2(items: list) -> list:
    """
    set(items) is not allowed
    """
    # can NOT deal with dict in list

    seen = set()
    result = []

    for x in items:
        # look up in set is O(1)
        if x not in seen:
            seen.add(x)
            result.append(x)

    return result


def remove_duplicates_v3(items: list) -> list:
    """
    set(items) is not allowed
    """
    # can NOT deal with dict in list

    # O(1), but this method must using python >= 3.7
    return list(dict.fromkeys(items))


def remove_duplicates_v4(items: list) -> list:
    """
    set(items) is not allowed
    """
    # can deal with dict in list
    # O(1), but need addition resourse for json dumps

    result = []
    seen = set()

    for x in items:
        str_x = json.dumps(x)
        if str_x not in seen:
            result.append(x)
            seen.add(str_x)

    return result


def find_duplicates(items: list) -> list:
    # O(n)
    seen = set()
    duplicated = set()
    result = []

    for x in items:
        if x in seen:
            if x not in duplicated:
                # keep the order
                result.append(x)
                duplicated.add(x)
        else:
            seen.add(x)

    return result


def invert_dict(data: dict) -> dict:
    result = {}

    for k, v in data.items():
        
        if v in result:
            result[v].append(k)
        else:
            result[v] = [k]

    return result


def invert_dict_v2(data: dict) -> dict:
    # defaultdict(list) can create a empty list [] as default value when the key doesn't exist

    result = defaultdict(list)

    for k, v in data.items():
        result[v].append(k)

    # convert defaultdict to dict
    return dict(result)


def invert_dict_v3(data: dict) -> dict:
    # using dict.setdefault(key, default) 
    result = {}

    for k, v in data.items():
        result.setdefault(v, []).append(k)

    return result


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    result = dict1.copy()

    for k, v in dict2.items():
        result[k] = v

    return result
            

def merge_dicts_v2(dict1: dict, dict2: dict) -> dict:
    result = dict1.copy()
    result.update(dict2) 

    return result


def merge_dicts_v3(dict1: dict, dict2: dict) -> dict:
    # required python 3.5+
    return {**dict1, **dict2}


def merge_dicts_v4(dict1: dict, dict2: dict) -> dict:
    # required python 3.9+
    return dict1 | dict2


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4, 1, 5, 3]))
    print(remove_duplicates_v2([1, 2, 3, 2, 4, 1, 5, 3]))
    print(remove_duplicates_v3([1, 2, 3, 2, 4, 1, 5, 3]))
    print(remove_duplicates_v4([1, 2, 3, 2, 4, 1, 5, 3]))
    print(remove_duplicates_v4([1, {"test": 123}, 3, {"test": 123}, 4, {"test": 123}, 5, 3]))
    
    print(find_duplicates(["a", "b", "c", "a", "d", "b", "a"]))

    print(invert_dict({
        "alice": "admin",
        "bob": "user",
        "charlie": "admin",
    }))

    print(invert_dict_v2({
        "alice": "admin",
        "bob": "user",
        "charlie": "admin",
    }))

    print(invert_dict_v3({
        "alice": "admin",
        "bob": "user",
        "charlie": "admin",
    }))

    dict1 = {
        "name": "Firefox",
        "version": "120",
        "size": 100,
    }

    dict2 = {
        "version": "121",
        "architecture": "amd64",
    }

    print(merge_dicts(dict1, dict2))
    print(merge_dicts_v2(dict1, dict2))
    print(merge_dicts_v3(dict1, dict2))
    print(merge_dicts_v4(dict1, dict2))
