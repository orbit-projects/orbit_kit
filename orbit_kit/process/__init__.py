"""
Orbit Process Utilities

Shared subprocess execution helpers.

Exports:
    normalize_command:
        Normalize subprocess arguments.

    run_process:
        Execute subprocess command.
"""

from .execution import (
    normalize_command,
    run_process,
)

__all__ = [
    "normalize_command",
    "run_process",
]
