"""
orbit_kit.process
~~~~~~~~~~~~~~~~~

Process execution utilities used throughout the
Orbit ecosystem.

This package provides a centralized interface for
executing external commands and interacting with
system processes.

Orbit packages should prefer these utilities over
direct usage of Python's ``subprocess`` module to
ensure consistent behavior and error handling.

Why This Package Exists
-----------------------
External process execution is required throughout
the Orbit ecosystem.

Examples include:

- Installing dependencies.
- Running development servers.
- Executing build commands.
- Running tests.
- Managing project templates.
- Interacting with external tooling.

Centralizing process execution provides:

- Consistent APIs.
- Standardized exceptions.
- Easier testing.
- Improved maintainability.
- Better developer experience.

Examples
--------
Execute a command::

    from orbit_kit.process import (
        run_process,
    )

    run_process(
        ["python", "--version"]
    )

Capture output::

    result = run_process(
        ["git", "--version"],
        capture_output=True,
    )

    print(result.stdout)

Public API
----------
normalize_command
    Normalize subprocess arguments.

run_process
    Execute a subprocess command.
"""

from .execution import (
    normalize_command,
    run_process,
)

__all__ = [
    "normalize_command",
    "run_process",
]
