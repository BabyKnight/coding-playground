from collections import Counter

def unique_packages(packages: list[dict]) -> list[dict]:
    """Remove duplicate package by name + architecture, only keep the packge when 1st time appear"""
    unique = set()
    res = []

    for pkg in packages:
        pkg_set = (pkg.get('name'), pkg.get('architecture'))

        if pkg_set in unique:
            continue
        unique.add(pkg_set)
        res.append(pkg)

    return res


def group_by_architecture(packages: list[dict]) -> dict:
    result = {}

    for pkg in packages:
        arch = pkg.get("architecture")

        if arch not in result:
            result[arch] = [pkg]
        else:
            result[arch].append(pkg)

    return result


def count_by_category(packages: list[dict]) -> dict:
    result = {}

    for pkg in packages:
        cat = pkg.get("category")

        result[cat] = result.get(cat, 0) + 1

    return result 



def count_by_category_v2(packages: list[dict]) -> dict:

    return dict(Counter(pkg.get("category") for pkg in packages))


def get_enabled_packages(packages: list[dict]) -> list[dict]:
    result = []

    for pkg in packages:
        if pkg.get("enabled"):
            result.append(pkg)

    return result


def find_package(packages: list[dict], name: str) -> list[dict]:
    result = []

    for pkg in packages:
        if name == pkg.get("name"):
            result.append(pkg)

    return result



def find_package_v2(packages: list[dict], name: str) -> list[dict]:
    return [pkg for pkg in packages if pkg.get("name") == name]


def generate_report(packages: list[dict]) -> dict:
    packages = unique_packages(packages)


    total = len(packages)

    # Using Generator Expression is simpler
    enabled = sum(1 for pkg in packages if pkg.get("enabled") is True)
    disabled = total - enabled

    #enabled = 0
    #disabled = 0

    arch = {}
    cate = {}

    for pkg in packages:
        #enabled_st = pkg.get("enabled")
        #if enabled_st:
        #    enabled += 1
        #else:
        #    disabled += 1

        pkg_arch = pkg.get("architecture")
        arch[pkg_arch] = arch.get(pkg_arch, 0) + 1

        pkg_cat = pkg.get("category")
        cate[pkg_cat] = cate.get(pkg_cat, 0) + 1

    return {
        "total": total,
        "enabled": enabled,
        "disabled": disabled,
        "architectures": arch,
        "categories": cate,
    }




if __name__ == "__main__":
    packages = [
        {
            "name": "firefox",
            "version": "120.0",
            "architecture": "amd64",
            "category": "browser",
            "enabled": True,
        },
        {
            "name": "chrome",
            "version": "121.0",
            "architecture": "amd64",
            "category": "browser",
            "enabled": True,
        },
        {
            "name": "vlc",
            "version": "3.0",
            "architecture": "arm64",
            "category": "media",
            "enabled": False,
        },
        {
            "name": "gimp",
            "version": "2.10",
            "architecture": "amd64",
            "category": "graphics",
            "enabled": True,
        },
        {
            "name": "vim",
            "version": "9.0",
            "architecture": "arm64",
            "category": "editor",
            "enabled": True,
        },
        {
            "name": "firefox",
            "version": "120.0",
            "architecture": "amd64",
            "category": "browser",
            "enabled": True,
        },
    ]


    print(unique_packages(packages))
    print(group_by_architecture(packages))
    print(count_by_category(packages))
    print(count_by_category_v2(packages))
    print(find_package(packages, "firefox"))
    print(find_package_v2(packages, "firefox"))
    print(generate_report(packages))


