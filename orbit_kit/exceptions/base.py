"""
orbit_kit.exceptions.base
~~~~~~~~~~~~~~~~~~~~~~~~~

Shared exception hierarchy used throughout the
Orbit Kit package.

Orbit Kit provides foundational utilities used by
multiple Orbit ecosystem packages. All package-
specific exceptions should inherit from
``OrbitKitError``.

Using a shared exception hierarchy enables:

- Consistent error handling
- Easier exception filtering
- Predictable framework behavior
- Better debugging and diagnostics

Exception Hierarchy
-------------------

OrbitKitError
├── ValidationError
├── ProcessError
├── FilesystemError
├── PathError
├── EnvironmentError
├── RuntimeEnvironmentError
└── ConsoleError
"""

from __future__ import annotations

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


class OrbitKitError(Exception):
    """
    Base exception for Orbit Kit.

    All Orbit Kit exceptions should inherit
    from this class.
    """

    default_message: str = "An Orbit Kit error occurred."

    def __init__(
        self,
        message: str | None = None,
    ) -> None:
        """
        Initialize the exception.

        Parameters
        ----------
        message:
            Optional custom exception message.
        """

        self.message: str = message or self.default_message

        super().__init__(self.message)

    def __str__(self) -> str:
        """
        Return the exception message.

        Returns
        -------
        str
            Human-readable exception message.
        """

        return self.message

    def __repr__(self) -> str:
        """
        Return a developer-friendly representation.

        Returns
        -------
        str
            Exception representation.
        """

        return f"{self.__class__.__name__}({self.message!r})"


class ValidationError(
    OrbitKitError,
):
    """
    Raised during validation failures.
    """

    default_message: str = "Validation failed."


class ProcessError(
    OrbitKitError,
):
    """
    Raised when process execution fails.
    """

    default_message: str = "Process execution failed."


class FilesystemError(
    OrbitKitError,
):
    """
    Raised when filesystem operations fail.
    """

    default_message: str = "Filesystem operation failed."


class PathError(
    OrbitKitError,
):
    """
    Raised when path resolution fails.
    """

    default_message: str = "Path operation failed."


class EnvironmentError(
    OrbitKitError,
):
    """
    Raised when environment inspection
    or detection fails.
    """

    default_message: str = "Environment operation failed."


class RuntimeEnvironmentError(
    OrbitKitError,
):
    """
    Raised when runtime information
    cannot be determined.
    """

    default_message: str = "Runtime inspection failed."


class ConsoleError(
    OrbitKitError,
):
    """
    Raised during console operations.
    """

    default_message: str = "Console operation failed."
