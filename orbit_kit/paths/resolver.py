"""
orbit_kit.paths.resolver
~~~~~~~~~~~~~~~~~~~~~~~~

Path resolution utilities used throughout the
Orbit ecosystem.

This module provides a centralized collection of
path-related helpers that are shared across Orbit
packages, developer tooling, project generators,
testing infrastructure, and runtime components.

Rather than interacting directly with ``pathlib``
throughout the codebase, Orbit components should
prefer these utilities whenever path discovery,
path normalization, or project location handling
is required.

Centralizing path operations provides several
benefits:

- Consistent path handling behavior.
- Reduced duplication across packages.
- Easier testing and mocking.
- Clearer project structure conventions.
- Future extensibility without widespread
  refactoring.

Design Goals
------------
The path utilities are designed to provide a
stable abstraction layer for filesystem location
management throughout the Orbit ecosystem.

This allows higher-level packages such as
Orbit CLI, Orbit Core, and Orbit Server to
rely on a predictable interface while remaining
isolated from implementation details.

As Orbit evolves, this module may become
responsible for:

- Project root discovery.
- Workspace detection.
- Package root resolution.
- Configuration file discovery.
- Runtime asset location.
- Template location handling.
- Build output path management.

Project Root Resolution
-----------------------
The current implementation returns the active
working directory as the project root.

Future versions may implement intelligent project
discovery by locating common project markers such
as:

- pyproject.toml
- .git
- orbit.toml
- workspace configuration files

This behavior would allow Orbit tooling to operate
correctly regardless of the user's current working
directory inside a project.

Examples
--------
Retrieve the current project root::

    from orbit_kit.paths import (
        project_root,
    )

    root = project_root()

Resolve a path::

    from orbit_kit.paths import (
        resolve_path,
    )

    path = resolve_path(
        "~/projects/orbit"
    )

Retrieve the current working directory::

    from orbit_kit.paths import (
        current_directory,
    )

    cwd = current_directory()

Functions
---------
current_directory
    Retrieve the current working directory.

project_root
    Retrieve the active Orbit project root.

resolve_path
    Resolve a path into an absolute filesystem
    location.
"""

from __future__ import annotations

from pathlib import Path

__all__ = [
    "current_directory",
    "project_root",
    "resolve_path",
]


def current_directory() -> Path:
    """
    Retrieve the current working directory.

    Returns
    -------
    Path
        Absolute path representing the current
        working directory.
    """

    return Path.cwd()


def project_root() -> Path:
    """
    Retrieve the current Orbit project root.

    Notes
    -----
    The current implementation returns the active
    working directory.

    Future implementations may perform project
    discovery by searching parent directories for
    known project markers such as ``pyproject.toml``
    or Orbit-specific configuration files.

    Returns
    -------
    Path
        Path representing the active project root.
    """

    return Path.cwd()


def resolve_path(
    path: str | Path,
) -> Path:
    """
    Resolve a filesystem path into an absolute path.

    This helper expands user directories and
    normalizes relative paths into absolute,
    fully-resolved filesystem locations.

    Parameters
    ----------
    path:
        Path to resolve.

    Returns
    -------
    Path
        Resolved absolute path.
    """

    return Path(path).expanduser().resolve()
