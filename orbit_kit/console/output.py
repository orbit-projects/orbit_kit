"""
orbit_kit.console.output
~~~~~~~~~~~~~~~~~~~~~~~~

Console output utilities used throughout the
Orbit ecosystem.

This module provides a centralized interface for
displaying formatted console messages.

Rather than interacting directly with terminal
rendering libraries, Orbit packages should use
these helpers to ensure consistent formatting,
styling, and user experience across the ecosystem.

Why This Module Exists
----------------------
Multiple Orbit packages need to display terminal
output.

Examples include:

- Orbit CLI commands.
- Project generators.
- Build tooling.
- Development workflows.
- Diagnostics utilities.
- Testing infrastructure.

By centralizing console output behavior, Orbit
can provide a consistent user experience while
keeping presentation logic separate from business
logic.

Design Goals
------------
The console layer is designed around several
principles:

- Consistency
    Messages should appear uniform throughout
    the ecosystem.

- Simplicity
    Common output operations should require
    minimal code.

- Maintainability
    Styling behavior should be defined in a
    single location.

- Extensibility
    Future rendering backends should be
    replaceable without changing callers.

Functions
---------
success
    Display a success message.

error
    Display an error message.

warning
    Display a warning message.

info
    Display an informational message.
"""

from __future__ import annotations

import typer

__all__ = [
    "success",
    "error",
    "warning",
    "info",
]


def success(
    message: str,
) -> None:
    """
    Display a success message.

    Success messages are typically used to
    indicate completed operations and positive
    outcomes.

    Parameters
    ----------
    message:
        Message to display.
    """

    typer.secho(
        message,
        fg=typer.colors.GREEN,
        bold=True,
    )


def error(
    message: str,
) -> None:
    """
    Display an error message.

    Error messages are typically used when an
    operation fails or requires user attention.

    Parameters
    ----------
    message:
        Message to display.
    """

    typer.secho(
        message,
        fg=typer.colors.RED,
        bold=True,
    )


def warning(
    message: str,
) -> None:
    """
    Display a warning message.

    Warning messages indicate potentially
    problematic situations that do not prevent
    execution.

    Parameters
    ----------
    message:
        Message to display.
    """

    typer.secho(
        message,
        fg=typer.colors.YELLOW,
        bold=True,
    )


def info(
    message: str,
) -> None:
    """
    Display an informational message.

    Informational messages provide context,
    progress updates, and general feedback.

    Parameters
    ----------
    message:
        Message to display.
    """

    typer.secho(
        message,
        fg=typer.colors.CYAN,
    )
