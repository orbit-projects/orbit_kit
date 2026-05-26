"""
Orbit Path Utilities

Shared filesystem path helpers.

Exports:
    project_root:
        Retrieve project root directory.
"""

from .resolver import (
    project_root,
)

__all__ = [
    "project_root",
]
