from collections.abc import Iterable, Iterator


def iter_batches(items: Iterable, batch_size: int) -> Iterator[list]:
    # check whether the batch_size is int and not bool
    if not isinstance(batch_size, int) or isinstance(batch_size, bool):
        raise ValueError("batch_size must be integer")

    if batch_size <= 0:
        raise ValueError("bathc_size must be greater than zero")

    # ----- Sometimes Iterable is not support len
    #for start in range(0, len(items), batch_size):
    #    yield items[start: start + batch_size]

    batch = []

    for item in items:
        batch.append(item)

        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch


def iter_packages(
        packages: Iterable[dict],
        channel: str | None = None,
        architecture: str | None = None,
    ) -> Iterator[dict]:

    result = []

    for batch in iter_batches(packages, 3):
        # batch contains <= 3 packages
        for pkg in batch:
            if channel is not None and pkg.get("channel") != channel:
                continue
            if architecture is not None and pkg.get("architecture") != architecture:
                continue

            result.append(pkg)

    return result


packages = [
    {
        "name": "firefox",
        "version": "120.0",
        "architecture": "amd64",
        "channel": "stable",
        "revision": 101
    },
    {
        "name": "vlc",
        "version": "3.0.20",
        "architecture": "amd64",
        "channel": "stable",
        "revision": 102
    },
    {
        "name": "firefox",
        "version": "121.0",
        "architecture": "arm64",
        "channel": "beta",
        "revision": 103
    },
    {
        "name": "chromium",
        "version": "119.0",
        "architecture": "arm64",
        "channel": "stable",
        "revision": 104
    },
]


if __name__ == "__main__":
    result = iter_packages(
        packages,
        channel="stable",
        architecture="amd64"
    )
    print("stable-amd64: expect [firefox, vlc]")
    for package in result:
        print(package["name"])


    result = iter_packages(packages)
    print("no filter: expect [firefox, vlc, firefox, chromium]")
    for package in result:
        print(package["name"])

    result = iter_packages(
        packages,
        channel="beta"
    )
    print("beta: expect [firefox]")
    for package in result:
        print(package["name"])

    result = iter_packages(
        packages,
        architecture="arm64"
    )
    print("arm64: expect [firefox, chromium]")
    for package in result:
        print(package["name"])


    items = [1, 2, 3, 4, 5]

    for batch in iter_batches(items, 2):
        print(batch)

    items = range(10)

    for batch in iter_batches(items, 3):
        print(batch)


    stable_packages = iter_packages(
        packages,
        channel="stable"
    )
    # firefox, vlc, chromium

    batches = iter_batches(
        stable_packages,
        batch_size=2
    )

    for batch in batches:
        print(batch)
