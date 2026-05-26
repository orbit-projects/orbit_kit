"""
Orbit Exception Utilities

Shared exception hierarchy used
throughout the Orbit ecosystem.

Exports:
    OrbitKitError:
        Base Orbit Kit exception.

    ValidationError:
        Validation failure exception.

    ProcessError:
        Process execution exception.
"""

from .base import (
    OrbitKitError,
    ProcessError,
    ValidationError,
)

__all__ = [
    "OrbitKitError",
    "ValidationError",
    "ProcessError",
]
