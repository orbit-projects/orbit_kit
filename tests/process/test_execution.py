"""
Tests for process execution utilities.

This module validates the subprocess execution
helpers used throughout the Orbit ecosystem.
"""

import sys
from pathlib import Path

import pytest

from orbit_kit.exceptions import (
    ProcessError,
)
from orbit_kit.process import (
    normalize_command,
    run_process,
)


def test_normalize_command_with_strings() -> None:
    """
    Verify string arguments remain unchanged.
    """

    command = [
        "python",
        "--version",
    ]

    assert (
        normalize_command(
            command,
        )
        == command
    )


def test_normalize_command_with_path_objects() -> None:
    """
    Verify Path objects are converted into
    strings.
    """

    command = [
        "python",
        Path("script.py"),
    ]

    result = normalize_command(
        command,
    )

    assert result == [
        "python",
        "script.py",
    ]


def test_run_process_success() -> None:
    """
    Verify successful process execution.
    """

    result = run_process(
        [
            sys.executable,
            "--version",
        ],
    )

    assert result.returncode == 0


def test_run_process_capture_output() -> None:
    """
    Verify process output can be captured.
    """

    result = run_process(
        [
            sys.executable,
            "-c",
            "print('orbit')",
        ],
        capture_output=True,
    )

    assert result.stdout.strip() == "orbit"


def test_run_process_with_cwd(
    tmp_path: Path,
) -> None:
    """
    Verify processes can execute within a
    specified working directory.
    """

    result = run_process(
        [
            sys.executable,
            "-c",
            "print('orbit')",
        ],
        cwd=tmp_path,
        capture_output=True,
    )

    assert result.returncode == 0


def test_run_process_invalid_command() -> None:
    """
    Verify invalid commands raise
    ProcessError.
    """

    with pytest.raises(
        ProcessError,
    ):
        run_process(
            [
                "orbit-command-does-not-exist",
            ],
        )
