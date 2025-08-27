"""Tests for pre_gen_project.py hook functions."""

import pytest
from hooks.pre_gen_project import (
    validate_no_spaces,
    validate_no_spaces_begin_or_end,
    validate_semantic_version,
    validate_https_url,
    validate_numbers_letters_hyphens,
)


def test_validate_no_spaces():
    """Validate no spaces in the arg_name"""
    validate_no_spaces("test", "test")
    validate_no_spaces("test-test", "test")
    validate_no_spaces("test_test.test", "test")


def test_validate_no_spaces_bad():
    """Validate no spaces in the arg_name bad"""
    with pytest.raises(SystemExit):
        validate_no_spaces("test test", "test")

    with pytest.raises(SystemExit):
        validate_no_spaces("test ", "test")

    with pytest.raises(SystemExit):
        validate_no_spaces(" test", "test")


def test_validate_no_spaces_begin_or_end():
    """Validate no spaces beginning or ending in the arg_name1d"""
    validate_no_spaces_begin_or_end("test test", "test")
    validate_no_spaces_begin_or_end("test test  test", "test")
    validate_no_spaces_begin_or_end("test test test", "test")


def test_validate_no_spaces_begin_or_end_bad():
    """Validate no spaces beginning or ending in the arg_name bad"""
    with pytest.raises(SystemExit):
        validate_no_spaces_begin_or_end(" test test", "test")

    with pytest.raises(SystemExit):
        validate_no_spaces_begin_or_end("test test ", "test")


def test_validate_semantic_version():
    """Validate semantic version in the arg_name"""
    validate_semantic_version("1.0.0", "test")
    validate_semantic_version("0.0.0", "test")
    validate_semantic_version("0.0.1", "test")
    validate_semantic_version("1.0.1", "test")
    validate_semantic_version("1.1.1", "test")
    validate_semantic_version("10.10.10", "test")


def test_validate_semantic_version_bad():
    """Validate semantic version in the arg_name bad"""
    with pytest.raises(SystemExit):
        validate_semantic_version("1.0", "test")

    with pytest.raises(SystemExit):
        validate_semantic_version("1.0.0-dev", "test")


def test_validate_https_url():
    """Validate https url in the arg_name"""
    validate_https_url("https://something.com", "test")


def test_validate_https_url_bad():
    """Validate https url in the arg_name bad"""
    with pytest.raises(SystemExit):
        validate_https_url("http://something.com", "test")

    with pytest.raises(SystemExit):
        validate_https_url("something.com", "test")


def test_validate_numbers_letters_hyphens():
    """Validate numbers letters hyphens in the arg_name"""
    validate_numbers_letters_hyphens("test", "test")
    validate_numbers_letters_hyphens("test-test", "test")
    validate_numbers_letters_hyphens("test-test-test", "test")
    validate_numbers_letters_hyphens("test-123-test", "test")
    validate_numbers_letters_hyphens("test-123-test-123", "test")
    validate_numbers_letters_hyphens("test-123-test-123-123", "test")


def test_validate_numbers_letters_hyphens_bad():
    """Validate numbers letters hyphens in the arg_name bad"""
    with pytest.raises(SystemExit):
        validate_numbers_letters_hyphens("test test", "test")

    with pytest.raises(SystemExit):
        validate_numbers_letters_hyphens("test_test", "test")

    with pytest.raises(SystemExit):
        validate_numbers_letters_hyphens("test.test", "test")
