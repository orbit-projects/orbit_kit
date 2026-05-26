"""
Filesystem Operations

Shared filesystem operations used
throughout the Orbit ecosystem.
"""

from pathlib import Path
import shutil


def ensure_directory(
    path: Path,
) -> None:
    """
    Ensure directory exists.
    """

    path.mkdir(
        parents=True,
        exist_ok=True,
    )


def remove_directory(
    path: Path,
) -> None:
    """
    Remove directory recursively.
    """

    if path.exists():
        shutil.rmtree(path)


def copy_directory(
    source: Path,
    destination: Path,
) -> None:
    """
    Copy directory recursively.
    """

    shutil.copytree(
        source,
        destination,
    )


def path_exists(
    path: Path,
) -> bool:
    """
    Determine whether path exists.
    """

    return path.exists()
