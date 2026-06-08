"""
Tests for path resolution utilities.

This module validates the path resolution helpers
used throughout the Orbit ecosystem.
"""

from pathlib import Path

from orbit_kit.paths import (
    current_directory,
    project_root,
    resolve_path,
)


def test_current_directory_returns_path() -> None:
    """
    Verify current_directory returns a Path.
    """

    result = current_directory()

    assert isinstance(
        result,
        Path,
    )


def test_current_directory_exists() -> None:
    """
    Verify the current directory exists.
    """

    result = current_directory()

    assert result.exists()


def test_project_root_returns_path() -> None:
    """
    Verify project_root returns a Path.
    """

    result = project_root()

    assert isinstance(
        result,
        Path,
    )


def test_project_root_exists() -> None:
    """
    Verify project_root returns an existing path.
    """

    result = project_root()

    assert result.exists()


def test_resolve_path_returns_absolute_path() -> None:
    """
    Verify relative paths are resolved into
    absolute filesystem paths.
    """

    result = resolve_path(
        ".",
    )

    assert result.is_absolute()


def test_resolve_path_returns_path_instance() -> None:
    """
    Verify resolve_path returns a Path object.
    """

    result = resolve_path(
        ".",
    )

    assert isinstance(
        result,
        Path,
    )


def test_resolve_path_with_path_object() -> None:
    """
    Verify Path instances are accepted.
    """

    result = resolve_path(
        Path("."),
    )

    assert isinstance(
        result,
        Path,
    )


def test_resolve_path_expands_user_directory() -> None:
    """
    Verify user directory expansion works.
    """

    result = resolve_path(
        "~",
    )

    assert result.exists()
