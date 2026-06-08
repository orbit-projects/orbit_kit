"""
orbit_kit.environment.detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Environment detection utilities used throughout the
Orbit ecosystem.

This module provides helpers for inspecting the
current runtime environment and locating external
tooling required by Orbit packages.

Environment inspection is primarily used by:

- Orbit CLI
- Project generators
- Development tooling
- Build systems
- Testing infrastructure

The goal of this module is to centralize environment
detection logic and provide a consistent interface
for runtime discovery.

Features
--------
- Python runtime discovery
- Node.js runtime discovery
- Frontend package manager detection

Future Responsibilities
-----------------------
As Orbit evolves this module may expand to support:

- Operating system detection
- Shell detection
- CI environment detection
- Git discovery
- Package manager discovery
- Container environment detection

Functions
---------
python_executable
    Retrieve the active Python executable.

detect_node
    Detect the Node.js runtime.

detect_package_manager
    Detect the frontend package manager used by
    a project.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

__all__ = [
    "python_executable",
    "detect_node",
    "detect_package_manager",
]

type PathLike = str | Path


def python_executable() -> str:
    """
    Retrieve the active Python executable.

    Returns
    -------
    str
        Absolute path to the active Python
        interpreter.
    """

    return sys.executable


def detect_node() -> str | None:
    """
    Detect the Node.js runtime.

    Returns
    -------
    str | None
        Path to the Node.js executable if found,
        otherwise None.
    """

    return shutil.which("node")


def detect_package_manager(
    directory: PathLike,
) -> str:
    """
    Detect the preferred frontend package manager.

    Detection is based on lockfile discovery.

    Detection Priority
    ------------------
    1. pnpm
    2. yarn
    3. npm

    Parameters
    ----------
    directory:
        Project directory.

    Returns
    -------
    str
        Detected package manager name.
    """

    directory = Path(directory)

    if (directory / "pnpm-lock.yaml").exists():
        return "pnpm"

    if (directory / "yarn.lock").exists():
        return "yarn"

    return "npm"
