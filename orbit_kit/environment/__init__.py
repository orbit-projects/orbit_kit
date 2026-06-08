"""
orbit_kit.environment
~~~~~~~~~~~~~~~~~~~~~

Environment detection utilities used throughout the
Orbit ecosystem.

This package provides helpers for inspecting the
current runtime environment, discovering external
tooling, and determining project-specific runtime
requirements.

Why This Package Exists
-----------------------
Orbit tooling frequently needs to interact with
external runtimes and development environments.

Examples include:

- Python discovery
- Node.js discovery
- Package manager detection
- Build tooling inspection
- Runtime validation

Centralizing this functionality provides a
consistent and maintainable approach to
environment inspection.

Examples
--------
Retrieve the active Python interpreter::

    from orbit_kit.environment import (
        python_executable,
    )

    executable = python_executable()

Detect Node.js::

    from orbit_kit.environment import (
        detect_node,
    )

    node = detect_node()

Detect a package manager::

    from orbit_kit.environment import (
        detect_package_manager,
    )

    manager = detect_package_manager(
        project_root,
    )

Public API
----------
python_executable
    Retrieve the active Python executable.

detect_node
    Detect the Node.js runtime.

detect_package_manager
    Detect the frontend package manager.
"""

from .detection import (
    detect_node,
    detect_package_manager,
    python_executable,
)

__all__ = [
    "python_executable",
    "detect_node",
    "detect_package_manager",
]
