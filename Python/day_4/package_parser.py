import logging
import json

from collections.abc import Iterable, Iterator
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class PackageRecordError(ValueError):
    """Raise when error for PackageRecord"""


@dataclass(frozen=True)
class PackageRecord:
    name: str
    version: str
    architecture: str
    channel: str

    def __post_init__(self) -> None:
        if any(
            not isinstance(x, str)
            or x is None
            or not x.strip()
            for x in (self.name, self.version, self.architecture, self.channel)
        ):
            raise PackageRecordError("arg of PackageRecord must be non-emptystring")


def parse_package_record(raw: str, line_number: int) -> PackageRecord:
    """Parse JSON for a single record"""
    try:
        pkg_record = json.loads(raw)
    except:
        #raise JSONDecodeError("Raw string cannot be decoded as Dictionary")
        raise PackageRecordError(f"Line {line_number} Raw string decode error.")

    if not isinstance(pkg_record, dict):
        raise PackageRecordError(f"Line {line_number} Raw string parse result is not a Dictionary.")
    if any(x not in pkg_record for x in ("name", "version", "architecture", "channel")):
        raise PackageRecordError(f"Line {line_number} Missing field in parsed package record.")
    if any(
            not isinstance(pkg_record.get(x), str)
            or pkg_record.get(x) is None
            or not pkg_record.get(x).strip()
            for x in ("name", "version", "architecture", "channel")
    ):
        raise PackageRecordError(f"Line {line_number} parsed package record contains empty string in values")

    return PackageRecord(
            pkg_record.get("name"),
            pkg_record.get("version"),
            pkg_record.get("architecture"),
            pkg_record.get("channel"),
    )


def iter_package_feed(lines: Iterable[str], *, skip_invalid: bool = False) -> Iterator[PackageRecord]:

    line_num = 0
    for line in lines:
        line_num += 1

        if not line:
            continue

        try:
            pkg_record = parse_package_record(line, line_number=line_num)
            yield pkg_record
        except Exception as e:
            if skip_invalid:
                logger.warning(f"WARNING: Invalid package record at line {line_num}")
                continue
            raise


if __name__ == "__main__":
    try:
        pr = PackageRecord("firefox", "120.0", "amd64", "stable")
        #pr = PackageRecord("firefox", "120.0", "amd64",)
        #pr = PackageRecord("firefox", 120.0, "amd64", "stable")
        #pr = PackageRecord()
    except:
        pass

    raw = '{"name": "firefox", "version": "120.0", "architecture": "amd64", "channel": "stable"}'

    record = parse_package_record(raw, line_number=1)

    print(record)
