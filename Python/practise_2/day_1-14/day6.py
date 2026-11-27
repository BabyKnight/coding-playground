


# Problem 1
def generate_numbers(start: int, stop: int):
    current = start
    while current < stop:
        yield current
        current += 1

# Problem 2
def package_generator():
    print("Generator started")

    yield "firefox"

    print("Generating vim")

    yield "vim"

    print("Generator finished")

# Problem 3
def get_enabled_package_names(packages: list[dict]):
    """List Comprehension"""
    return [pkg["name"].upper() for pkg in packages if pkg["enabled"] == True]

def get_enabled_package_names_v2(packages: list[dict]):
    """Generator Expression"""
    return (pkg["name"].upper() for pkg in packages if pkg["enabled"] == True)

# Problem 4
def flatten_groups(groups):
    for group in groups:
        yield from group


# Problem 5
def generator_a():
    yield [1, 2, 3]


def generator_b():
    yield from [1, 2, 3]


# Problem 6
def flatten_nested(items):
    for item in items:
        if isinstance(item, list):
            yield from flatten_nested(item)
        else:
            yield item

# Problem 8
def package_processor():
    pkg = None
    
    while True:
        received = yield pkg

        if received is not None:
            pkg = received["name"].upper()
        else:
            pkg = None

# Problem 11
def filter_enabled(packages):
    return (pkg for pkg in packages if pkg["enabled"] == True)


def filter_by_size(packages, min_size):
    return (pkg for pkg in packages if pkg["size"] >= min_size)


def extract_names(packages):
    return (pkg["name"].upper() for pkg in packages)


# Problem 12
def iter_batches(items, batch_size):

    if batch_size <= 0:
        raise ValueError("batch size must be >= 0")

    batch = []
    for item in items:
        batch.append(item)
        if len(batch) >= batch_size:
            yield batch
            batch = []

    if batch:
        yield batch


# Problem 13

class PackageRepository:

    def __init__(self, packages):
        self.packages = list(packages)

    def iter_packages(self):
        return iter(self.packages)

    def iter_enabled(self):
        return (pkg for pkg in self.packages if pkg["enabled"] == True)

    def iter_by_architecture(self, architecture):
        return (pkg for pkg in self.packages if pkg["architecture"] == architecture)

    def iter_by_size(self, min_size):
        return (pkg for pkg in self.packages if pkg["size"] >= min_size)

    def iter_package_names(self):
        return (pkg["name"].upper() for pkg in self.packages)


    def iter_batches(self, batch_size):
        if batch_size <= 0:
            raise ValueError("batch size must be positive integer")
        
        batch = []
        for pkg in self.packages:
            batch.append(pkg)

            if len(batch) >= batch_size:
                yield batch
                batch = []

        if batch:
            yield batch


if __name__ == "__main__":
    print(list(generate_numbers(1, 5)))

    gen = package_generator()

    print("A")
    print(next(gen))

    print("B")
    print(next(gen))

    print("C")

    try:
        print(next(gen))
    except StopIteration:
        print("Finished")


    packages = [
        {"name": "firefox", "enabled": True},
        {"name": "vim", "enabled": False},
        {"name": "vlc", "enabled": True},
        {"name": "git", "enabled": True},
    ]

    print(get_enabled_package_names(packages))
    print(get_enabled_package_names_v2(packages))
    print(list(get_enabled_package_names_v2(packages)))

    groups = [
        ["firefox", "vim"],
        ["vlc", "git"],
        ["nano", "curl"],
    ]

    res = flatten_groups(groups)
    for i in res:
        print(i)
    print(list(flatten_groups(groups)))

    items = [
        1,
        [2, 3],
        [4, [5, 6]],
        7,
        [[8, 9], 10],
    ]
    res = flatten_nested(items)
    for i in res:
        print(i)
    print(list(flatten_nested(items)))


    processor = package_processor()

    next(processor)

    print(processor.send({"name": "firefox"}))
    print(processor.send({"name": "vim"}))
    print(processor.send({"name": "vlc"}))

    packages = [
        {"name": "firefox", "enabled": True, "size": 120},
        {"name": "vim", "enabled": False, "size": 50},
        {"name": "vlc", "enabled": True, "size": 200},
        {"name": "git", "enabled": True, "size": 80},
        {"name": "nano", "enabled": True, "size": 150},
    ]


    result = extract_names(
    filter_by_size(
        filter_enabled(packages),
        100
        )
    )

    print(list(result))


    items = range(1, 11)

    print(list(iter_batches(items, 3)))


    packages = [
        {
            "name": "firefox",
            "version": "120.0",
            "architecture": "amd64",
            "enabled": True,
            "size": 120,
        },
        {
            "name": "vim",
            "version": "9.0",
            "architecture": "amd64",
            "enabled": False,
            "size": 50,
        },
        {
            "name": "vlc",
            "version": "3.0",
            "architecture": "arm64",
            "enabled": True,
            "size": 200,
        },
        {
            "name": "git",
            "version": "2.4",
            "architecture": "amd64",
            "enabled": True,
            "size": 80,
        },
        {
            "name": "nano",
            "version": "7.0",
            "architecture": "arm64",
            "enabled": True,
            "size": 150,
        },
    ]

    repo = PackageRepository(packages)

    print(list(repo.iter_enabled()))

    print(list(repo.iter_by_architecture("amd64")))

    print(list(repo.iter_by_size(100)))

    print(list(repo.iter_package_names()))

    print(list(repo.iter_batches(2)))

    result = repo.iter_enabled()

    result = filter_by_size(result, 100)

    result = extract_names(result)

    print(list(result))
