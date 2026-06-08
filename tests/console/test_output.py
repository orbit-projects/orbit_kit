"""
Tests for console output utilities.

This module validates the console helpers used
throughout the Orbit ecosystem.
"""

from unittest.mock import patch

import typer

from orbit_kit.console import (
    error,
    info,
    success,
    warning,
)


def test_success_output() -> None:
    """
    Verify success messages are rendered using
    the expected configuration.
    """

    with patch(
        "orbit_kit.console.output.typer.secho",
    ) as mock_secho:
        success(
            "Operation completed.",
        )

        mock_secho.assert_called_once_with(
            "Operation completed.",
            fg=typer.colors.GREEN,
            bold=True,
        )


def test_error_output() -> None:
    """
    Verify error messages are rendered using
    the expected configuration.
    """

    with patch(
        "orbit_kit.console.output.typer.secho",
    ) as mock_secho:
        error(
            "Operation failed.",
        )

        mock_secho.assert_called_once_with(
            "Operation failed.",
            fg=typer.colors.RED,
            bold=True,
        )


def test_warning_output() -> None:
    """
    Verify warning messages are rendered using
    the expected configuration.
    """

    with patch(
        "orbit_kit.console.output.typer.secho",
    ) as mock_secho:
        warning(
            "Potential issue detected.",
        )

        mock_secho.assert_called_once_with(
            "Potential issue detected.",
            fg=typer.colors.YELLOW,
            bold=True,
        )


def test_info_output() -> None:
    """
    Verify informational messages are rendered
    using the expected configuration.
    """

    with patch(
        "orbit_kit.console.output.typer.secho",
    ) as mock_secho:
        info(
            "Processing request.",
        )

        mock_secho.assert_called_once_with(
            "Processing request.",
            fg=typer.colors.CYAN,
        )
