"""
Process Execution Utilities

Shared subprocess execution helpers
used throughout Orbit.
"""

from pathlib import Path
import subprocess


def normalize_command(
    command: list[str | Path],
) -> list[str]:
    """
    Normalize subprocess command arguments.
    """

    return [str(part) for part in command]


def run_process(
    command: list[str | Path],
    cwd: Path | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess:
    """
    Execute subprocess command.
    """

    normalized_command = normalize_command(command)

    return subprocess.run(
        normalized_command,
        cwd=str(cwd) if cwd else None,
        check=check,
    )
