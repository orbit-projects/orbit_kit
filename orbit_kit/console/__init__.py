"""
Orbit Console Utilities

Shared terminal and console helpers
used throughout the Orbit ecosystem.

Exports:
    success:
        Display success messages.

    error:
        Display error messages.

    warning:
        Display warning messages.

    info:
        Display informational messages.
"""

from .output import (
    error,
    info,
    success,
    warning,
)

__all__ = [
    "success",
    "error",
    "warning",
    "info",
]
