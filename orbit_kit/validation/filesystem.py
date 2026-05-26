"""
Filesystem Validation Utilities

Shared filesystem validation helpers.
"""

from pathlib import Path

from orbit_kit.exceptions import (
    ValidationError,
)


def validate_directory(
    path: Path,
) -> None:
    """
    Validate directory existence.

    Args:
        path:
            Target directory path.

    Raises:
        ValidationError:
            If directory does not exist.
    """

    if not path.exists():
        raise ValidationError(f"Directory does not exist: {path}")

    if not path.is_dir():
        raise ValidationError(f"Path is not a directory: {path}")
