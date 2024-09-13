from typing import TypedDict

class YarnLockDependency(TypedDict):
    matches: list[str]
    version: str
    resolved: str
    integrity: str
    dependencies: dict[str, str]
    optionalDependencies: dict[str, str]

def yarnlock_parse(yarnlock: str, /) -> dict[str, YarnLockDependency]: ...