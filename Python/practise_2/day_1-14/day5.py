from collections.abc import Iterable, Iterator


# Problem 1

def inspect_objects(objects: list) -> list[tuple[bool, bool]]:
    res = []

    for obj in objects:
        res.append((isinstance(obj, Iterable), isinstance(obj, Iterator)))

    return res

# Problem 2

def consume_iterator(items: list[int]) -> list[int]:
    
    res = []
    iter_items = iter(items)
    while True:
        try:
            res.append(next(iter_items))
        except StopIteration:
            break

    return res

# Problem 3

def read_iterator(items: list[int]) -> tuple[list[int], list[int]]:
    iterator_t = iter(items)


    res_1 = [i for i in iterator_t]
    res_2 = [i for i in iterator_t]

    return (res_1, res_2)

# Problem 4

class PackageIterator:

    def __init__(self, packages: list[dict]):
        self.packages = packages
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.packages):
            raise StopIteration
        pkg = self.packages[self.index]
        self.index += 1

        return pkg

# Problem 5

class NumberRangeIterator:

    def __init__(
        self,
        start: int,
        stop: int,
        step: int = 1
    ):
        self.start = start
        self.stop = stop
        if step == 0:
            raise ValueError("step cannot be 0")
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.current >= self.stop:
                raise StopIteration
        
        else:
            if self.current <= self.stop:
                raise StopIteration

        val = self.current
        self.current += self.step

        return val

# Problem 6

class PackageCollection:

    def __init__(self, packages: list[dict]):
        self.packages = packages

    def __iter__(self):
        return iter(self.packages)

# Problem 7

class PackageRepositoryIterator:

    def __init__(self, packages):
        self.packages = packages
        self.index = 0

    def __iter__(self):
        if self.index >= len(self.packages):
            raise StopIteration

        pkg = self.packages[index]
        self.index += 1

        return pkg


class PackageRepository:

    def __init__(self, packages):
        self.packages = packages

    def __iter__(self):
        return PackageRepositoryIterator(self.packages)


# Problem 8

def read_until_stop():
    data = ["firefox", "vim", "vlc", "STOP"]
    index = 0

    def fetch():
        nonlocal index
        val = data[index]
        index += 1
        return val

    res = iter(fetch, "STOP")
    return res

# Problem 9

def process_packages(packages: list[dict]):
    return iter(
        pkg["name"].upper() for pkg in packages
        if pkg["enabled"] == True
        and pkg["size"] >= 100
    )

# Problem 10

class PackageRepository:

    def __init__(self, packages: list[dict]):
        self.packages = packages

    def __iter__(self):
        return iter(self.packages)

    def iter_enabled(self):
        return (pkg for pkg in self.packages if pkg["enabled"] == True)

    def iter_by_architecture(self, architecture: str):
        return (pkg for pkg in self.packages if pkg["architecture"] == architecture)

    def get_package_count(self) -> int:
        return len(self.packages)




if __name__ == "__main__":
    objects = [
        [1, 2, 3],
        (1, 2, 3),
        {"a": 1, "b": 2},
        {1, 2, 3},
        "hello",
        iter([1, 2, 3]),
        100
    ]

    print(inspect_objects(objects))

    print(consume_iterator([10, 20, 30]))

    print(read_iterator([1, 2, 3, 4]))

    print([i for i in read_until_stop()])


    packages = [
        {"name": "firefox", "size": 120, "enabled": True},
        {"name": "vim", "size": 50, "enabled": True},
        {"name": "vlc", "size": 200, "enabled": False},
        {"name": "chrome", "size": 300, "enabled": True},
        {"name": "git", "size": 80, "enabled": True}
    ]
    print([i for i in process_packages(packages)])
