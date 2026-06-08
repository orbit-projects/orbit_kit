"""
orbit_kit.exceptions
~~~~~~~~~~~~~~~~~~~~

Public exception exports for Orbit Kit.

This package provides the shared exception hierarchy
used throughout the Orbit Kit package and related
Orbit ecosystem components.

Applications and internal Orbit packages should
generally import exceptions from this module rather
than individual implementation files.

Examples
--------
Catch all Orbit Kit exceptions::

    from orbit_kit.exceptions import (
        OrbitKitError,
    )

    try:
        ...
    except OrbitKitError:
        ...

Catch specific exceptions::

    from orbit_kit.exceptions import (
        ValidationError,
    )

    raise ValidationError(
        "Invalid configuration."
    )

Exports
-------
OrbitKitError
    Base Orbit Kit exception.

ValidationError
    Raised when validation operations fail.

ProcessError
    Raised when process execution fails.

FilesystemError
    Raised when filesystem operations fail.

PathError
    Raised when path operations fail.

EnvironmentError
    Raised when environment detection fails.

RuntimeEnvironmentError
    Raised when runtime inspection fails.

ConsoleError
    Raised when console operations fail.
"""

from .base import (
    ConsoleError,
    EnvironmentError,
    FilesystemError,
    OrbitKitError,
    PathError,
    ProcessError,
    RuntimeEnvironmentError,
    ValidationError,
)

__all__ = [
    "OrbitKitError",
    "ValidationError",
    "ProcessError",
    "FilesystemError",
    "PathError",
    "EnvironmentError",
    "RuntimeEnvironmentError",
    "ConsoleError",
]
