from collections import Counter


def find_packages(packages, name=None, architecture=None, channel=None):
    """Find packages matching all provided filters."""

    result = []

    for pkg in packages:
        if name is not None and pkg.get("name") != name:
            continue
        if architecture is not None and pkg.get("architecture") != architecture:
            continue
        if channel is not None and pkg.get("channel") != channel:
            continue

        result.append(pkg)

    return result


def count_packages_by_architecture(packages):
    """Count packages by atchitchture."""

    counts = Counter(
            pkg["architecture"]
            for pkg in packages
            if "architecture" in pkg
    )
    
    return dict(counts)


def parse_version(version):
    parts = version.split(".")

    if not parts or any(not part.isdigit() for part in parts):
        raise ValueError(f"Invalid version: {version}")

    return tuple(int(part) for part in parts)


def get_latest_packages(packages):
    """"Return the latest version of each package name."""

    latest = {}

    for pkg in packages:
        name  = pkg.get("name")
        version = pkg.get("version")

        if not name or not version:
            continue

        try:
            current_version = parse_version(version)
        except ValueError:
            continue

        existing = latest.get("name")

        if existing is None:
            latest[name] = pkg
            continue

        existing_version = parse_version(existing["version"])

        if current_version > existing_version:
            latest[name] = pkg

    return list(latest.values())


if __name__ == "__main__":
    print(find_packages(packages, 'firefox'))
    print(find_packages(packages, architecture='amd64'))
    print(find_packages(packages, architecture='stable'))
    print(find_packages(packages, 'firefox', 'amd64'))
    print(find_packages(packages, 'firefox', 'amd64', 'stable'))
    print(find_packages(packages, 'firefox', channel='stable'))
    print(find_packages(packages, architecture='amd64', channel='stable'))

    print(count_packages_by_architecture(packages))

    print(get_latest_packages(packages))

