from collections import Counter

# Problem 1

def process_numbers(numbers: list[int]) -> list[int]:
    return [x*x for x in numbers if x % 2 != 0 and x*x > 20]


def process_numbers_v2(numbers: list[int]) -> list[int]:
    return [temp for x in numbers if x % 2 != 0 and (temp:=x*x) > 20]

def process_numbers_v3(numbers: list[int]) -> list[int]:
    result = []

    for x in numbers:
        if x % 2 != 0:
            temp = x * x
            if temp > 20:
                result.append(temp)
    return result


# Problem 2

def build_package_index(packages: list[dict]) -> dict:
    return {pkg['name']:pkg['version']
            for pkg in packages
            if pkg.get("name") is not None and pkg.get("version") is not None
    }


# Problem 3

def get_architectures(packages: list[dict]) -> set[str]:
    return set(pkg["architecture"] for pkg in packages if pkg.get("architecture") is not None)



# Problem 4

def sort_packages(packages: list[dict]) -> list[dict]:
    return sorted(packages, key = lambda x: x.get("size", 0))

def sort_packages_reverse(packages: list[dict]) -> list[dict]:
    return sorted(packages, key = lambda x: x.get("size", 0), reverse = True)


# Problem 5

def sort_packages(packages: list[dict]) -> list[dict]:
    return sorted(packages, key = lambda x: (x.get("architecture"), -x.get("size", 0), x.get("name")) )


# Problem 6

def sort_versions(versions: list[str]) -> list[str]:
    return sorted(versions, key = lambda x: tuple(int(item) for item in x.split(".")))


# Problem 7

def has_disabled_package(packages: list[dict]) -> bool:
    return any(not pkg.get("enabled") for pkg in packages)


def all_packages_enabled(packages: list[dict]) -> bool:
    return all(pkg.get("enabled") for pkg in packages)

# Problem 8

def process_numbers_8(numbers: list[int]) -> list[int]:
    return list(map(lambda x: x * x, list(filter(lambda x: x % 2 == 0, numbers))))

def process_numbers_8_list_comprehension(numbers: list[int]) -> list[int]:
    return [x * x for x in numbers if x % 2 == 0]


# Problem 9

def sum_with_list(numbers) -> int:
    # memory O(k)
    return sum([x for x in numbers if x % 2 ==0])


def sum_with_generator(numbers) -> int:
    # memory O(1)
    # BETTER!  especially in super set of the numbers
    return sum(x for x in numbers if x % 2 ==0)


# Problem 10

def process_packages(packages: list[dict]):
    # yield
    for pkg in packages:
        if pkg.get("enabled") and pkg.get("size") >= 100:
            yield pkg["name"].upper()

def process_packages_v2(packages: list[dict]):
    # generator
    return (x.get("name").upper() for x in packages if x.get("enabled") and x.get("size") >= 100)


# Problem 11

def filter_packages(
    packages: list[dict],
    architecture: str | None = None,
    enabled: bool | None = None,
    min_size: int | None = None,
) -> list[dict]:
    return [pkg for pkg in packages 
            if (architecture is None or pkg.get("architecture") == architecture)
            and (enabled is None or pkg.get("enabled") == enabled)
            and (min_size is None or pkg.get("size") >= min_size)
    ]


def sort_packages_pkg(
    packages: list[dict],
    descending: bool = False,
) -> list[dict]:
    return sorted(packages, key = lambda x: x.get("size"), reverse= descending)


def get_package_names(packages: list[dict]) -> list[str]:
    return list({x.get("name").upper():None for x in packages if x.get("enabled")}.keys())


def get_package_statistics(packages: list[dict]) -> dict:
    total = len(packages)
    enabled = sum(1 for pkg in packages if pkg.get("enabled") is True)
    
    arch = dict(Counter(pkg.get("architecture") for pkg in packages))
    avg = sum(pkg.get("size") for pkg in packages) / total

    return {
        "total": total,
        "enabled": enabled,
        "disabled": total - enabled,
        "architectures": arch,
        "average_size": avg,
    }



if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(process_numbers(numbers))
    print(process_numbers_v2(numbers))
    print(process_numbers_v3(numbers))

    packages = [
        {"name": "firefox", "version": "120.0"},
        {"name": "chrome", "version": "121.0"},
        {"name": "vlc", "version": "3.0"},
        {"name": "vim", "version": "9.0"},
    ]

    print(build_package_index(packages))

    packages = [
        {"name": "firefox", "architecture": "amd64"},
        {"name": "chrome", "architecture": "amd64"},
        {"name": "vlc", "architecture": "arm64"},
        {"name": "vim", "architecture": "arm64"},
        {"name": "gimp", "architecture": "amd64"},
    ]
    print(get_architectures(packages))

    packages = [
        {"name": "firefox", "size": 120},
        {"name": "chrome", "size": 250},
        {"name": "vlc", "size": 80},
        {"name": "gimp", "size": 180},
    ]
    print(sort_packages(packages))
    print(sort_packages_reverse(packages))


    packages = [
        {"name": "firefox", "architecture": "amd64", "size": 120},
        {"name": "chrome", "architecture": "amd64", "size": 250},
        {"name": "vlc", "architecture": "arm64", "size": 80},
        {"name": "gimp", "architecture": "amd64", "size": 180},
        {"name": "vim", "architecture": "arm64", "size": 80},
    ]
    print(sort_packages(packages))


    versions = [
        "1.2.0",
        "1.10.0",
        "1.3.5",
        "2.0.0",
        "1.2.10",
        "1.2.3",
    ]

    print(sort_versions(versions))

    packages = [
        {"name": "firefox", "enabled": True},
        {"name": "chrome", "enabled": True},
        {"name": "vlc", "enabled": False},
    ]

    print(has_disabled_package(packages))  # True
    print(all_packages_enabled(packages))  # False


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(process_numbers_8(numbers))
    print(process_numbers_8_list_comprehension(numbers))

    numbers = range(1, 1000001)
    print(sum_with_list(numbers))
    print(sum_with_generator(numbers))


    packages = [
        {"name": "firefox", "size": 120, "enabled": True},
        {"name": "chrome", "size": 250, "enabled": False},
        {"name": "vlc", "size": 80, "enabled": True},
        {"name": "gimp", "size": 180, "enabled": True},
        {"name": "vim", "size": 50, "enabled": False},
    ]
    print("yield>>>>")
    res = process_packages(packages)
    for i in res:
        print(i)

    print("Generator>>>>")
    res = process_packages_v2(packages)
    for i in res:
        print(i)


    packages = [
        {
            "name": "firefox",
            "version": "120.0",
            "architecture": "amd64",
            "size": 120,
            "enabled": True,
        },
        {
            "name": "chrome",
            "version": "121.0",
            "architecture": "amd64",
            "size": 250,
            "enabled": False,
        },
        {
            "name": "vlc",
            "version": "3.0",
            "architecture": "arm64",
            "size": 80,
            "enabled": True,
        },
        {
            "name": "gimp",
            "version": "2.10",
            "architecture": "amd64",
            "size": 180,
            "enabled": True,
        },
        {
            "name": "vim",
            "version": "9.0",
            "architecture": "arm64",
            "size": 50,
            "enabled": True,
        },
        {
            "name": "firefox",
            "version": "121.0",
            "architecture": "amd64",
            "size": 130,
            "enabled": True,
        },
    ]

    print(filter_packages(packages))
    print(sort_packages_pkg(packages, True))
    print(sort_packages_pkg(packages, False))

    print(get_package_names(packages))

    print(get_package_statistics(packages))
