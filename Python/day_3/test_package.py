import pytest

from package import (iter_batches, iter_packages)


@pytest.fixture
def packages():
    return [
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


def test_iter_batches():
    result = iter_batches([1, 2, 3, 4, 5], 2)
    assert next(result) == [1, 2]
    assert next(result) == [3, 4]
    assert next(result) == [5]


def test_iter_batches_with_range():
    result = iter_batches(range(10), 3)
    assert next(result) == [0, 1, 2]
    assert next(result) == [3, 4, 5]
    assert next(result) == [6, 7, 8]
    assert next(result) == [9]


@pytest.mark.parametrize("batch", ["3", True, -1])
def test_iter_batches_with_invalid_batchsize(batch):
    with pytest.raises(ValueError):
        result = iter_batches([1, 2, 3, 4, 5], batch)
        next(result)


def test_iter_packages_by_channel_arch(packages):
    result = iter_packages(packages, channel="stable", architecture="amd64")

    assert [pkg["name"] for pkg in result] == ["firefox", "vlc"]


def test_iter_packages_without_filter(packages):
    result = list(iter_packages(packages))

    assert result == packages


def test_iter_packages_by_channel(packages):
    result = iter_packages(packages, channel="beta")

    assert [pkg["name"] for pkg in result] == ["firefox"]


def test_iter_packages_by_architecture(packages):
    result = iter_packages(packages, architecture="arm64")

    assert [pkg["name"] for pkg in result] == ["firefox", "chromium"]

