from abc import ABC, abstractmethod
from functools import total_ordering

class Package():
    def __init__(self, name: str, version: str, architecture: str, enabled: bool = False):
        self.name = name
        self.version = version
        self.architecture = architecture
        self.enabled = enabled

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False

    def get_info(self) -> dict[st, str | bool]:
        return {
            "name": self.name,
            "version": self.version,
            "architecture": self.architecture,
            "enabled": self.enabled
        }



class Package2():
    package_count = 0

    def __init__(self, name: str):
        self.name = name
        #Package2.package_count += 1
        type(self).package_count += 1

    @classmethod
    def get_package_count(cls) -> int:
        #return Package2.package_count
        return cls.package_count

    def get_name(self) -> str:
        return self.name


class Package3():

    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        if not value:
            raise ValueError("Version cannot be empty string or None")
        self._version = value


class Package4():
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def install(self):
        raise NotImplementedError
    #print({
    #        "pkg": self.__class__.__name__,
    #        "name": self.name,
    #        "version": self.version,
    #    })

    def uninstall():
        raise NotImplementedError


class DebianPackage(Package4):
    def install(self) -> None:
        print(f"Installing Debian package: {self.name}")

    def uninstall(self) -> None:
        print(f"Uninstalling Debian package: {self.name}")

    
class SnapPackage(Package4):
    def install(self) -> None:
        print(f"Installing Snap package: {self.name}")

    def uninstall(self) -> None:
        print(f"Uninstalling Snap package: {self.name}")


class FlatpakPackage(Package4):
    def install(self) -> None:
        print(f"Installing Flatpak package: {self.name}")

    def uninstall(self) -> None:
        print(f"Uninstalling Flatpak package: {self.name}")


class PackageManager(ABC):
    
    def __init__(self) -> None:
        self.installed = []

    @abstractmethod
    def install(self) -> None:
        pass

    @abstractmethod
    def uninstall(self) -> None:
        pass
        
    def list_installed_packages(self):
        return self.installed.copy()


class DebianPackageManager(PackageManager):

    def install(self, pkg_name):
        print(f"Installing Debian package: {pkg_name}")
        self.installed.append(pkg_name)

    def uninstall(self, pkg_name):
        print(f"Uninstalling Debian package: {pkg_name}")
        if pkg_name not in self.installed:
            raise ValueError
        self.installed.remove(pkg_name)

class SnapPackageManager(PackageManager):

    def install(self, pkg_name):
        print(f"Installing Snap package: {pkg_name}")
        self.installed.append(pkg_name)

    def uninstall(self, pkg_name):
        print(f"Uninstalling Snap package: {pkg_name}")
        if pkg_name not in self.installed:
            raise ValueError
        self.installed.remove(pkg_name)


class Package5():
    def __init__(self, name: str, version: str):
        self.name = name
        self.version_str = version
        self.version = tuple(self.version_str.split("."))


    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        return self.name == other.name and self.version == other.version 

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        if self.name != other.name:
            return NotImplemented
        return self.version < other.version

    def __repr__(self):
        return f'Package5("{self.name}","{self.version_str}")'

class PackageRepository:

    def __init__(self, packages):
        self._packages = list(packages)

    def __getitem__(self, index):
        return self._packages[index]

    def __iter__(self):
        return iter(self._packages)

    def __contains__(self, package):
        return package in self._packages

class Packages6:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return f"Packages6: {self.name} v{self.version}"

    def __repr__(self):
        return f"Packages6(name={repr(self.name)}, version={repr(self.version)})"


if __name__ == "__main__":
    pkg = Package(
        name="firefox",
        version="120.0",
        architecture="amd64"
    )

    pkg.enable()
    print(pkg.get_info())

    pkg1 = Package2("firefox")
    pkg2 = Package2("vim")
    pkg3 = Package2("python3")

    print(Package2.get_package_count())  # 3

    pkg = Package3("firefox", "120.0")

    print(pkg.version)

    pkg.version = "121.0"

    print(pkg.version)

    packages = [
        DebianPackage("firefox", "120.0"),
        SnapPackage("code", "1.85"),
        FlatpakPackage("gimp", "3.0"),
    ]

    for pkg in packages:
        pkg.install()

    manager = DebianPackageManager()

    manager.install("firefox")
    print(f"installed packages --- {manager.list_installed_packages()}")
    manager.install("vim")
    print(f"installed packages --- {manager.list_installed_packages()}")
    manager.uninstall("firefox")
    print(f"installed packages --- {manager.list_installed_packages()}")
    manager.install("vlc")
    print(f"installed packages --- {manager.list_installed_packages()}")


    pkg1 = Package5("firefox", "120.0")
    pkg2 = Package5("firefox", "121.0")

    print(pkg1 == pkg2)
    print(pkg1 < pkg2)
    print(pkg1 > pkg2)

    pkg = Packages6("dla", "1.2.2")
    print(str(pkg))
    print(repr(pkg))
