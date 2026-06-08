"""
orbit_kit.console
~~~~~~~~~~~~~~~~~

Console output utilities used throughout the
Orbit ecosystem.

This package provides a centralized interface for
displaying terminal output and user-facing messages.

Orbit packages should prefer these utilities over
direct interaction with rendering libraries to
ensure a consistent developer experience.

Examples
--------
Display a success message::

    from orbit_kit.console import (
        success,
    )

    success(
        "Project created successfully."
    )

Display an error message::

    from orbit_kit.console import (
        error,
    )

    error(
        "Build failed."
    )

Display informational output::

    from orbit_kit.console import (
        info,
    )

    info(
        "Installing dependencies..."
    )

Public API
----------
success
    Display a success message.

error
    Display an error message.

warning
    Display a warning message.

info
    Display an informational message.

plain
    Display an unformatted message.
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
