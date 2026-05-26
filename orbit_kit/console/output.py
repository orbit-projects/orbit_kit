"""
Console Output Utilities

Provides shared console output helpers
for Orbit ecosystem packages.
"""

import typer


def success(
    message: str,
) -> None:
    """
    Display success message.
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
    Display error message.
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
    Display warning message.
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
    Display informational message.
    """

    typer.secho(
        message,
        fg=typer.colors.CYAN,
    )
