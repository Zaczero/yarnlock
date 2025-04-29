import json
from pathlib import Path

from yarnlock import yarnlock_parse


def _run_test_from_dir(dir_name):
    yarnlock, yarnlock_expected = _load_yarnlock_and_yarnlock_expected(
        dir_name=dir_name
    )
    assert yarnlock_parse(yarnlock) == yarnlock_expected


def _load_yarnlock_and_yarnlock_expected(dir_name):
    yarnlock = Path("tests", dir_name, "yarn.lock").read_text()
    yarnlock_expected = json.loads(
        Path("tests", dir_name, "yarn.lock.json").read_bytes()
    )
    return yarnlock, yarnlock_expected


def test_parse_empty_yarn_lock_file():
    _run_test_from_dir("empty_yarn_lock_file")


def test_parse_only_whitespace_yarn_lock_file():
    _run_test_from_dir("only_whitespace_yarn_lock_file")


# TODO: the complex_yarn_lock_file.json fixture needs to be specified correctly
# before uncommenting and running this function. It is currently empty until determined.
# def test_parse_complex_yarn_lock_file():
#     _run_test_from_dir("complex_yarn_lock_file")


def test_parse_package_with_missing_semantic_version_range():
    _run_test_from_dir("package_with_missing_semantic_version_range")


def test_parse_package_with_multiple_resolved_versions():
    _run_test_from_dir("package_with_multiple_resolved_versions")


def test_parse_package_with_multiple_semantic_version_ranges():
    _run_test_from_dir("package_with_multiple_semantic_version_ranges")


def test_parse_package_with_at_symbol_prefix():
    _run_test_from_dir("package_with_at_symbol_prefix")
