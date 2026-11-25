from collections import Counter
from collections import defaultdict
from collections import deque

# Problem 1

def count_elements(items: list[str]) -> dict[str, int]:
    return dict(Counter(items))

# Problem 2

def get_top_n(
    items: list[str],
    n: int = 3
) -> list[tuple[str, int]]:
    return Counter(items).most_common(n)

# Problem 3

def merge_counts(a: list[str], b: list[str]) -> dict:
    return Counter(a) + Counter(b)


def common_counts(a: list[str], b: list[str]) -> dict:
    return Counter(a) & Counter(b)

def subtract_counts(a: list[str], b: list[str]) -> dict:
    return Counter(a) - Counter(b)


# Problem 4


def group_packages_by_architecture(
    packages: list[dict]
) -> dict[str, list[str]]:
    res = defaultdict(list)

    for pkg in packages:
        if "architecture" not in pkg or "name" not in pkg:
            continue
        res[pkg.get("architecture")].append(pkg.get("name"))

    return dict(res)

# Problem 5

def group_packages(
    packages: list[dict]
) -> dict[str, dict[str, list[str]]]:
    res = defaultdict(lambda: defaultdict(list))

    for pkg in packages:
        res[pkg["architecture"]][pkg["category"]].append(pkg["name"])

    return {k:dict(v) for k,v in res.items()}

# Problem 6

class PackageQueue:

    def __init__(self):
        self.que = deque()

    def enqueue(self, package: str) -> None:
        self.que.append(package)

    def dequeue(self) -> str | None:
        if len(self.que) == 0:
            return None
        res = self.que.popleft()
        return res

    def peek(self) -> str | None:
        if len(self.que) == 0:
            return None
        return self.que[0]

    def is_empty(self) -> bool:
        return len(self.que) == 0

    def size(self) -> int:
        return len(self.que)


# Problem 7

class PackageHistory:

    def __init__(self, max_size: int = 5):
        self.que = deque()
        self.max_size = max_size

    def add(self, package: str) -> None:
        if len(self.que) == self.max_size:
            self.que.popleft()
        self.que.append(package)


    def get_history(self) -> list[str]:
        return list(self.que)

# Problem 8

def count_log_levels(logs: list[str]) -> dict[str, int]:
    return dict(Counter([log.split(" ")[0] for log in logs]))

def get_error_packages(logs: list[str]) -> list[str]:
    return  [log.split(" ")[2] for log in logs if log.split(" ")[0] == "ERROR"]

def get_top_error_package(logs: list[str]) -> str | None:
    pass




if __name__ == "__main__":

    items = [
        "amd64", "arm64", "amd64",
        "arm64", "amd64", "riscv64"
    ]

    print(count_elements(items))

    packages = [
        "firefox", "vim", "firefox",
        "vlc", "vim", "firefox",
        "chrome", "vim", "vlc"
    ]
    print(get_top_n(packages))

    packages_a = [
        "firefox", "vim", "vlc",
        "firefox", "chrome"
    ]

    packages_b = [
        "firefox", "vim", "chrome",
        "chrome", "git"
    ]

    print(merge_counts(packages_a, packages_b))
    print(common_counts(packages_a, packages_b))
    print(subtract_counts(packages_a, packages_b))


    packages = [
        {"name": "firefox", "architecture": "amd64"},
        {"name": "vim", "architecture": "arm64"},
        {"name": "vlc", "architecture": "amd64"},
        {"name": "git", "architecture": "arm64"},
        {"name": "chrome", "architecture": "amd64"}
    ]
    print(group_packages_by_architecture(packages))


    packages = [
        {"name": "firefox", "architecture": "amd64", "category": "browser"},
        {"name": "chrome", "architecture": "amd64", "category": "browser"},
        {"name": "vim", "architecture": "arm64", "category": "editor"},
        {"name": "nano", "architecture": "amd64", "category": "editor"},
        {"name": "vlc", "architecture": "arm64", "category": "media"}
    ]
    print(group_packages(packages))

    queue = PackageQueue()

    queue.enqueue("firefox")
    queue.enqueue("vim")
    queue.enqueue("vlc")

    print(queue.dequeue())  # firefox
    print(queue.peek())     # vim
    print(queue.size())     # 2
    print(queue.is_empty()) # False

    history = PackageHistory(max_size=3)

    history.add("firefox")
    history.add("vim")
    history.add("vlc")
    history.add("chrome")

    print(history.get_history())

    logs = [
        "INFO Package firefox installed",
        "ERROR Package vim installation failed",
        "INFO Package vlc installed",
        "WARNING Package chrome update delayed",
        "ERROR Package git installation failed",
        "INFO Package vim installed",
        "ERROR Package vlc installation failed"
    ]
    print(count_log_levels(logs))
    print(get_error_packages(logs))
    print(get_top_error_package(logs))
    

