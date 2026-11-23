from dataclasses import dataclass


VALID_CHANNELS = {
    "stable",
    "candidate",
    "beta",
    "edge",
}


class PackageError(Exception):
    """Base exception for package-related errors."""


class InvalidRevisionError(PackageError):
    """Raise when revision data is invalid."""


class DuplicateRevisionError(PackageError):
    """Raise when a revision number already exists."""


class RevisionNotFoundError(PackageError):
    """Raise when a revision cannot be found."""


class InvalidChannelError(PackageError):
    """Raise when an unsupported channel is used."""


@dataclass(frozen=True)
class Revision:
    number: int
    version: str
    architecture: str

    def __post_init__(self) -> None:
        if type(self.number) is not int or self.number <= 0:
            raise InvalidRevisionError(
                    "Revision number must be a positive integer"
            )

        if not isinstance(self.version, str) or not self.version.strip():
            raise InvalidRevisionError(
                    "Version must be a non-empty string"
            )

        if not isinstance(self.architecture, str) or not self.architecture.strip():
            raise InvalidRevisionError(
                    "Architecture must be a non-empty string"
            )


class Package:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"Package name cannot be empty")

        self.name = name

        # revision number -> Revision
        self._revisions: dict[int, Revision] = {}

        # channel -> architecture -> Revision
        self._releases: dict[str, dict[str, Revision]] = {}


    def add_revision(self, revision: Revision) -> None:
        if not isinstance(revision, Revision):
            raise TypeError("revision must be a Revision instance")

        if revision.number in self._revisions:
            raise DuplicateRevisionError(
                f"Revision {revision.number} already exists"
            )

        self._revisions[revision.number] = revision


    def promote(self, revision_number: int, channel: str) -> None:
        if channel not in VALID_CHANNELS:
            raise InvalidChannelError(
                f"unsupported channel: {channel}"
            )

        revision = self._revisions.get(revision_number)

        if revision is None:
            raise RevisionNotFoundError(
                f"Revision {revision_number} does not exist"
            )

        if channel not in self._releases:
            self._releases[channel] = {}

        # update release for this channel and architecture
        self._releases[channel][revision.architecture] = revision


    def get_release(self, channel: str, architecture: str) -> Revision | None:
        if channel not in VALID_CHANNELS:
            raise InvalidChannelError(
                f"unsupported channel: {channel}"
            )

        return self._releases.get(channel, {}).get(architecture)


if __name__ == "__main__":
    firefox = Package("firefox")

    firefox.add_revision(
        Revision(101, "120.0", "amd64")
    )

    firefox.add_revision(
        Revision(102, "121.0", "arm64")
    )

    firefox.add_revision(
        Revision(103, "122.0", "amd64")
    )

    firefox.promote(101, "stable")
    firefox.promote(102, "beta")
    firefox.promote(103, "stable")

    print(firefox.get_release("stable", "amd64"))
    # Revision(number=103, version='122.0', architecture='amd64')

    print(firefox.get_release("beta", "arm64"))
    # Revision(number=102, version='121.0', architecture='arm64')

    print(firefox.get_release("stable", "arm64"))
    # None
