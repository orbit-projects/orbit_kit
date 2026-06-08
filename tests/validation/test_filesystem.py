"""
Tests for filesystem validation utilities.

This module validates the filesystem validation
helpers used throughout the Orbit ecosystem.
"""

from pathlib import Path

import pytest

from orbit_kit.exceptions import (
    ValidationError,
)
from orbit_kit.validation import (
    validate_directory,
    validate_exists,
    validate_file,
)


def test_validate_exists_with_existing_path(
    tmp_path: Path,
) -> None:
    """
    Verify existing paths pass validation.
    """

    result = validate_exists(
        tmp_path,
    )

    assert result == tmp_path


def test_validate_exists_with_missing_path(
    tmp_path: Path,
) -> None:
    """
    Verify missing paths raise ValidationError.
    """

    missing_path = tmp_path / "missing"

    with pytest.raises(
        ValidationError,
    ):
        validate_exists(
            missing_path,
        )


def test_validate_directory_with_directory(
    tmp_path: Path,
) -> None:
    """
    Verify directories pass validation.
    """

    result = validate_directory(
        tmp_path,
    )

    assert result == tmp_path


def test_validate_directory_with_file(
    tmp_path: Path,
) -> None:
    """
    Verify files fail directory validation.
    """

    file_path = tmp_path / "test.txt"

    file_path.write_text(
        "orbit",
        encoding="utf-8",
    )

    with pytest.raises(
        ValidationError,
    ):
        validate_directory(
            file_path,
        )


def test_validate_directory_with_missing_path(
    tmp_path: Path,
) -> None:
    """
    Verify missing directories raise errors.
    """

    directory = tmp_path / "missing"

    with pytest.raises(
        ValidationError,
    ):
        validate_directory(
            directory,
        )


def test_validate_file_with_file(
    tmp_path: Path,
) -> None:
    """
    Verify files pass validation.
    """

    file_path = tmp_path / "orbit.txt"

    file_path.write_text(
        "orbit",
        encoding="utf-8",
    )

    result = validate_file(
        file_path,
    )

    assert result == file_path


def test_validate_file_with_directory(
    tmp_path: Path,
) -> None:
    """
    Verify directories fail file validation.
    """

    with pytest.raises(
        ValidationError,
    ):
        validate_file(
            tmp_path,
        )


def test_validate_file_with_missing_file(
    tmp_path: Path,
) -> None:
    """
    Verify missing files raise ValidationError.
    """

    file_path = tmp_path / "missing.txt"

    with pytest.raises(
        ValidationError,
    ):
        validate_file(
            file_path,
        )
