

from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


# Problem 1

def iter_batches(
    items: Iterable[T],
    batch_size: int
) -> Iterator[list[T]]:
    if batch_size <= 0:
        raise ValueError("Batch size must be positive integer")
    batch = []

    for item in items:
        batch.append(item)

        if len(batch) >= batch_size:
            yield batch
            batch = []

    if batch:
        yield batch


# Problem 2
class PackageIterator:

    def __init__(self, packages, architecture=None):
        self.packages = packages
        self.arch = architecture
        self.index = 0 # to mark the current index during iteration

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.packages):
            pkg = self.packages[self.index]
            self.index += 1
            
            if self.arch is None or pkg["architecture"] == self.arch:
                return pkg

        raise StopIteration

# Problem 3
class PackageCollection:

    def __init__(self, packages):
        self.packages = packages

    def __iter__(self):
        for pkg in self.packages:
            yield pkg
        
# Problem 7
def iter_log_lines(lines):
    #for line in lines:
    #    yield line
    yield from lines

def filter_error_logs(lines):
    return (line for line in lines if line.split() and line.split()[0] == "ERROR")


def extract_error_messages(lines):
    #return (err_msg.split(maxsplit=1)[1] for err_msg in lines if err_msg.split()[0] == "ERROR")
    for line in lines:
        parts = line.split(maxsplit=1)

        if len(parts) == 2 and parts[0] == "ERROR":
            yield parts[1]


if __name__ == "__main__":
    items = range(1, 11)

    print(list(iter_batches(items, 3)))

    packages = [
        {"name": "firefox", "architecture": "amd64"},
        {"name": "vlc", "architecture": "arm64"},
        {"name": "vim", "architecture": "amd64"},
        {"name": "git", "architecture": "arm64"},
    ]

    iterator = PackageIterator(packages, "amd64")

    print(list(iterator))


    collection = PackageCollection(packages)

    print(list(collection))
    print(list(collection))

    logs = [
        "INFO firefox started",
        "ERROR firefox failed to launch",
        "WARNING vim configuration missing",
        "ERROR vlc segmentation fault",
        "INFO git repository updated",
        "ERROR apt package installation failed",
    ]

    print(list(iter_log_lines(logs)))
    print(list(filter_error_logs(logs)))
    print(list(extract_error_messages(logs)))
