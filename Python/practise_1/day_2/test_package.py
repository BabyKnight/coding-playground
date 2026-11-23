import pytest

from package import (
    Package,
    Revision,
    InvalidRevisionError,
    DuplicateRevisionError,
    RevisionNotFoundError,
    InvalidChannelError,
)

@pytest.fixture
def package():
    return Package("fixrfox")

@pytest.fixture
def revisions():
    return [
        Revision(101, "120.0", "amd64"),
        Revision(102, "121.0", "arm64"),
        Revision(103, "122.0", "amd64"),
    ]


# -------------------------
# Revision tests
# -------------------------

def test_create_valid_revision():
    revision = Revision(101, "120.0", "amd64")

    assert revision.number == 101
    assert revision.version == "120.0"
    assert revision.architecture == "amd64"


@pytest.mark.parametrize("number", ["101", -1, 0, 1.5, True, False])
def test_invalid_version_number(number):
    with pytest.raises(InvalidRevisionError):
        Revision(number, "120.0", "amd64")


@pytest.mark.parametrize("version", ["", "   ", 123, None])
def test_invalid_version(version):
    with pytest.raises(InvalidRevisionError):
        Revision(120, version, "amd64")


@pytest.mark.parametrize("arch", ["", "   ", 123, None])
def  test_invalid_architecture(arch):
    with pytest.raises(InvalidRevisionError):
        Revision(120, "120.0", arch)


def test_revision_is_immutable():
    revision = Revision(101, "120.0", "amd64")

    with pytest.raises(AttributeError):
        revision.version = "122.0"


# -------------------------
# Package tests
# -------------------------
def test_create_package():
    pkg = Package("firefox")

    assert pkg.name == "firefox"


@pytest.mark.parametrize("name", ["", "  ", None, 123])
def test_invalid_package_name(name):
    with pytest.raises(ValueError):
        Package(name)


def test_add_revision(package, revisions):
    package.add_revision(revisions[0])

    assert package._revisions[101] == revisions[0]


def test_add_invalid_revision(package):
    with pytest.raises(TypeError):
        package.add_revision({"number": 101})


def test_add_duplicate_revision(package, revisions):
    package.add_revision(revisions[0])

    with pytest.raises(DuplicateRevisionError):
        package.add_revision(revisions[0])


# -------------------------
# Channel tests
# -------------------------

def test_promote_revision(package, revisions):
    package.add_revision(revisions[0])

    package.promote(101, "stable")

    result = package.get_release("stable", "amd64")
    assert result == revisions[0]


@pytest.mark.parametrize("channel", ["unknown", "probudtion", "", None])
def test_promote_invalid_channel(package, channel):
    with pytest.raises(InvalidChannelError):
        package.promote(101, channel)


def test_promote_nonexistent_revision(package):
    with pytest.raises(RevisionNotFoundError):
        package.promote(999, "stable")



def test_promotr_updates_existing_release(package, revisions):
    for revision in revisions:
        package.add_revision(revision)

    package.promote(101, "stable")
    package.promote(103, "stable")

    result = package.get_release("stable", "amd64")

    assert result == revisions[2]


# -------------------------
# Query tests
# -------------------------

def test_get_nonexistent_release(package):
    assert package.get_release("stable", "amd64") is None


def test_get_release_from_invalid_channel(package):
    with pytest.raises(InvalidChannelError):
        package.get_release("production", "amd64")

