# test_day1.py

import pytest

from day1 import (
        find_packages,
        count_packages_by_architecture,
        parse_version,
        get_latest_packages,
    )


@pytest.fixture
def packages():
    return [
        {
            "name": "firefox",
            "version": "120.0",
            "architecture": "amd64",
            "channel": "stable",
        },
        {
            "name": "vlc",
            "version": "3.0.20",
            "architecture": "amd64",
            "channel": "stable",
        },
        {
            "name": "firefox",
            "version": "121.0",
            "architecture": "arm64",
            "channel": "beta",
        },
        {
            "name": "chromium",
            "version": "119.0",
            "architecture": "amd64",
            "channel": "stable",
        },
        {
            "name": "firefox",
            "version": "122.0",
            "architecture": "amd64",
            "channel": "edge",
        },
    ]


# -----------------------------------------
#  Task 1: find_packages
# -----------------------------------------

def test_find_packages_by_name(packages):
    result = find_packages(packages, name="firefox")

    assert len(result) == 3
    assert all(pkg['name'] == "firefox" for pkg in result)


def test_find_packages_by_architecture(packages):
    result = find_packages(packages, architecture="arm64")

    assert len(result) == 1
    assert result[0]["name"] == "firefox"


def test_find_packages_by_channel(packages):
    result = find_packages(packages, channel="stable")

    assert len(result) == 3
    assert all(pkg["channel"] == "stable" for pkg in result)


def test_find_packages_with_multiple_filters(packages):
    result = find_packages(
        packages,
        name="firefox",
        architecture="amd64",
        channel="stable",
    )

    assert len(result) == 1
    assert result[0]["version"] == "120.0"


def test_find_packages_without_filters(packages):
    result = find_packages(packages)

    assert len(result) == 5
    assert result == packages


def test_find_packages_empty_list():
    assert find_packages([]) == []


# -----------------------------------------
#  Task 2: count_packages_by_architecture
# -----------------------------------------

def test_count_packages_by_architecture(packages):
    result = count_packages_by_architecture(packages)

    assert result == {
            "amd64": 4,
            "arm64": 1,
            }


# -----------------------------------------
#  Task 3: get_latest_packages
# -----------------------------------------

def test_get_latest_packages(packages):
    result = get_latest_packages(packages)

    assert result == [
        {
            "name": "firefox",
            "version": "122.0",
            "architecture": "amd64",
            "channel": "edge",
        },
        {
            "name": "vlc",
            "version": "3.0.20",
            "architecture": "amd64",
            "channel": "stable",
        },
        {
            "name": "chromium",
            "version": "119.0",
            "architecture": "amd64",
            "channel": "stable",
        },
    ] 
