"""
orbit_kit.validation.filesystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filesystem validation utilities used throughout the
Orbit ecosystem.

This module provides reusable validation helpers for
filesystem paths and locations.

The goal of these utilities is to centralize common
filesystem validation logic and provide consistent
error messages across Orbit packages.

Rather than duplicating path validation checks
throughout the codebase, Orbit components should
prefer these helpers whenever validating filesystem
resources.

Functions
---------
validate_exists
    Validate path existence.

validate_directory
    Validate directory existence.

validate_file
    Validate file existence.
"""

from __future__ import annotations

from pathlib import Path

from orbit_kit.exceptions import (
    ValidationError,
)

__all__ = [
    "validate_exists",
    "validate_directory",
    "validate_file",
]

type PathLike = str | Path


def validate_exists(
    path: PathLike,
) -> Path:
    """
    Validate that a path exists.

    Parameters
    ----------
    path:
        Path to validate.

    Returns
    -------
    Path
        Validated path object.

    Raises
    ------
    ValidationError
        If the path does not exist.
    """

    path = Path(path)

    if not path.exists():
        raise ValidationError(f"Path does not exist: {path}")

    return path


def validate_directory(
    path: PathLike,
) -> Path:
    """
    Validate that a directory exists.

    Parameters
    ----------
    path:
        Directory path.

    Returns
    -------
    Path
        Validated directory path.

    Raises
    ------
    ValidationError
        If the directory does not exist or the
        path is not a directory.
    """

    path = validate_exists(path)

    if not path.is_dir():
        raise ValidationError(f"Path is not a directory: {path}")

    return path


def validate_file(
    path: PathLike,
) -> Path:
    """
    Validate that a file exists.

    Parameters
    ----------
    path:
        File path.

    Returns
    -------
    Path
        Validated file path.

    Raises
    ------
    ValidationError
        If the file does not exist or the path
        is not a file.
    """

    path = validate_exists(path)

    if not path.is_file():
        raise ValidationError(f"Path is not a file: {path}")

    return path
