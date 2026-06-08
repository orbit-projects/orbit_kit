"""
orbit_kit.filesystem.operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filesystem operations used throughout the Orbit
ecosystem.

This module provides a consistent abstraction over
common filesystem tasks and normalizes filesystem
errors into Orbit-specific exceptions.

The goal is to centralize filesystem behavior and
avoid duplicated logic across Orbit packages.

Functions
---------
ensure_directory
    Create a directory if it does not exist.

remove_directory
    Remove a directory recursively.

copy_directory
    Copy a directory recursively.

read_file
    Read file contents.

write_file
    Write file contents.

path_exists
    Determine whether a path exists.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from orbit_kit.exceptions import (
    FilesystemError,
)

__all__ = [
    "ensure_directory",
    "remove_directory",
    "copy_directory",
    "read_file",
    "write_file",
    "path_exists",
]

type PathLike = str | Path


def ensure_directory(
    path: PathLike,
) -> Path:
    """
    Ensure a directory exists.

    Parameters
    ----------
    path:
        Directory path.

    Returns
    -------
    Path
        Resolved directory path.
    """

    path = Path(path)

    try:
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
    except OSError as exc:
        raise FilesystemError(f"Failed to create directory: {path}") from exc

    return path


def remove_directory(
    path: PathLike,
) -> None:
    """
    Remove a directory recursively.

    Parameters
    ----------
    path:
        Directory path.
    """

    path = Path(path)

    try:
        if path.exists():
            shutil.rmtree(path)
    except OSError as exc:
        raise FilesystemError(f"Failed to remove directory: {path}") from exc


def copy_directory(
    source: PathLike,
    destination: PathLike,
) -> Path:
    """
    Copy a directory recursively.

    Parameters
    ----------
    source:
        Source directory.

    destination:
        Destination directory.

    Returns
    -------
    Path
        Destination path.
    """

    source = Path(source)
    destination = Path(destination)

    try:
        shutil.copytree(
            source,
            destination,
        )
    except OSError as exc:
        raise FilesystemError(
            f"Failed to copy directory from {source} to {destination}"
        ) from exc

    return destination


def read_file(
    path: PathLike,
    *,
    encoding: str = "utf-8",
) -> str:
    """
    Read a text file.

    Parameters
    ----------
    path:
        File path.

    encoding:
        File encoding.

    Returns
    -------
    str
        File contents.
    """

    path = Path(path)

    try:
        return path.read_text(
            encoding=encoding,
        )
    except OSError as exc:
        raise FilesystemError(f"Failed to read file: {path}") from exc


def write_file(
    path: PathLike,
    content: str,
    *,
    encoding: str = "utf-8",
) -> Path:
    """
    Write text to a file.

    Parameters
    ----------
    path:
        File path.

    content:
        Content to write.

    encoding:
        File encoding.

    Returns
    -------
    Path
        Written file path.
    """

    path = Path(path)

    try:
        path.write_text(
            content,
            encoding=encoding,
        )
    except OSError as exc:
        raise FilesystemError(f"Failed to write file: {path}") from exc

    return path


def path_exists(
    path: PathLike,
) -> bool:
    """
    Determine whether a path exists.

    Parameters
    ----------
    path:
        Path to inspect.

    Returns
    -------
    bool
        True if path exists.
    """

    return Path(path).exists()
