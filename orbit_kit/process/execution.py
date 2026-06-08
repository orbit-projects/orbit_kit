"""
orbit_kit.process.execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Process execution utilities used throughout the
Orbit ecosystem.

This module provides a centralized abstraction for
executing external processes and commands.

Rather than invoking ``subprocess`` directly
throughout the codebase, Orbit components should
prefer these utilities to ensure consistent
behavior, error handling, and developer experience.

The process utilities are heavily used by:

- Orbit CLI
- Project generators
- Template management
- Build tooling
- Testing infrastructure
- Development workflows

Design Goals
------------
The process layer exists to:

- Standardize process execution.
- Normalize process-related exceptions.
- Improve maintainability.
- Simplify testing and mocking.
- Provide a stable public API.

Functions
---------
normalize_command
    Normalize command arguments.

run_process
    Execute a subprocess command.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from orbit_kit.exceptions import (
    ProcessError,
)

__all__ = [
    "normalize_command",
    "run_process",
]

type PathLike = str | Path


def normalize_command(
    command: list[str | Path],
) -> list[str]:
    """
    Normalize subprocess command arguments.

    Parameters
    ----------
    command:
        Command argument sequence.

    Returns
    -------
    list[str]
        Normalized command arguments.
    """

    return [str(part) for part in command]


def run_process(
    command: list[str | Path],
    *,
    cwd: PathLike | None = None,
    check: bool = True,
    capture_output: bool = False,
) -> subprocess.CompletedProcess[str]:
    """
    Execute a subprocess command.

    Parameters
    ----------
    command:
        Command arguments.

    cwd:
        Working directory used during
        process execution.

    check:
        Raise an exception when the
        process exits with a non-zero
        status code.

    capture_output:
        Capture stdout and stderr.

    Returns
    -------
    subprocess.CompletedProcess[str]
        Process execution result.

    Raises
    ------
    ProcessError
        If process execution fails.
    """

    normalized_command = normalize_command(
        command,
    )

    try:
        return subprocess.run(
            normalized_command,
            cwd=str(cwd) if cwd is not None else None,
            check=check,
            capture_output=capture_output,
            text=True,
        )

    except (
        OSError,
        subprocess.SubprocessError,
    ) as exc:
        raise ProcessError(
            f"Failed to execute process: {' '.join(normalized_command)}"
        ) from exc
