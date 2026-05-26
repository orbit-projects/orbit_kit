"""
Orbit Filesystem Utilities

Shared filesystem abstractions and helpers.

Exports:
    ensure_directory:
        Ensure directory exists.

    remove_directory:
        Remove directory recursively.

    copy_directory:
        Copy directory recursively.

    path_exists:
        Determine whether path exists.
"""

from .operations import (
    copy_directory,
    ensure_directory,
    path_exists,
    remove_directory,
)

__all__ = [
    "ensure_directory",
    "remove_directory",
    "copy_directory",
    "path_exists",
]
