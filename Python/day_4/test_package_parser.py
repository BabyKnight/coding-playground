import pytest

from package_parser import (
    PackageRecordError,
    PackageRecord,
    parse_package_record,
)

@pytest.fixture
def raw():
    return '{"name": "firefox", "version": "120.0", "architecture": "amd64", "channel": "stable"}'


def test_packagerecord():
    result = PackageRecord("firefox", "120.0", "amd64", "stable")

    assert result.name == "firefox"
    assert result.version == "120.0"
    assert result.architecture == "amd64"
    assert result.channel == "stable"

    # assert if immutable
    with pytest.raises(AttributeError):
        result.version = "120.1"


@pytest.mark.parametrize(
        "name, version, arch, channel",
        [
            (None, "120.0", "amd64", "stable"),
            ("firefox", None, "amd64", "stable"),
            ("firefox", "120.0", None, "stable"),
            ("firefox", "120.0", "amd64", None),
            (None, None, None, None),
        ]
)
def test_packagerecord_with_missing_arg(name, version, arch, channel):
    with pytest.raises(PackageRecordError):
        result = PackageRecord(name, version, arch, channel)


@pytest.mark.parametrize(
        "name, version, arch, channel",
        [
            ("", "120.0", "amd64", "stable"),
            ("firefox", "    ", "amd64", "stable"),
            ("firefox", "120.0", "", "stable"),
            ("firefox", "120.0", "amd64", "\n"),
            ("        ", "", "   ", ""),
        ]
)
def test_packagerecord_with_empty_string(name, version, arch, channel):
    with pytest.raises(PackageRecordError):
        result = PackageRecord(name, version, arch, channel)


@pytest.mark.parametrize(
        "name, version, arch, channel",
        [
            (1, "120.0", "amd64", "stable"),
            ("firefox", 120.0, "amd64", "stable"),
            ("firefox", "120.0", True, "stable"),
            ("firefox", "120.0", "amd64", []),
        ]
)
def test_packagerecord_with_non_string(name, version, arch, channel):
    with pytest.raises(PackageRecordError):
        result = PackageRecord(name, version, arch, channel)


def test_parse_package_record():
    raw = '{"name": "firefox", "version": "120.0", "architecture": "amd64", "channel": "stable"}'
    result = parse_package_record(raw, line_number=1)

    assert result == PackageRecord("firefox", "120.0", "amd64", "stable")

@pytest.mark.parametrize(
    "raw",
    [
        '[{"name": "firefox", "version": "120.0", "architecture": "amd64", "channel": "stable"}]',
        '["firefox","120.0", "amd64", "stable"]',
    ]
)
def test_parse_package_record_not_dict(raw):
    with pytest.raises(PackageRecordError) as excinfo:
        result = parse_package_record(raw, line_number=1)

    assert "not a Dictionary" in str(excinfo.value)


def test_parse_package_record_non_json():
    raw = '"name": "firefox", "version": "120.0", "architecture": "amd64", "channel": "stable"}'
    with pytest.raises(PackageRecordError) as excinfo:
        result = parse_package_record(raw, line_number=1)

    assert "decode error" in str(excinfo.value)


@pytest.mark.parametrize(
    "raw",
    [
        '{"version": "120.0", "architecture": "amd64", "channel": "stable"}',
        '{"name": "firefox", "architecture": "amd64", "channel": "stable"}',
        '{"name": "firefox", "version": "120.0", "channel": "stable"}',
        '{"name": "firefox", "version": "120.0", "architecture": "amd64"}',
    ]
)
def test_parse_package_record_missing_field(raw):
    with pytest.raises(PackageRecordError) as excinfo:
        result = parse_package_record(raw, line_number=1)

    assert "Missing field" in str(excinfo.value)



@pytest.mark.parametrize(
    "raw",
    [
        '{"name": "", "version": "120.0", "architecture": "amd64", "channel": "stable"}',
        '{"name": "firefox", "version": 120.0, "architecture": "amd64", "channel": "stable"}',
        '{"name": "firefox", "version": "120.0", "architecture": "    ", "channel": "stable"}',
        '{"name": "firefox", "version": "120.0", "architecture": "amd64", "channel": ""}',
    ]
)
def test_parse_package_record_empty_value(raw):
    with pytest.raises(PackageRecordError) as excinfo:
        result = parse_package_record(raw, line_number=1)

    assert "contains empty string in values" in str(excinfo.value)




def test_iter_package_feed():
    pass


