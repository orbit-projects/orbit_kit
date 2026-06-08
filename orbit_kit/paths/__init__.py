"""
orbit_kit.paths
~~~~~~~~~~~~~~~

Path resolution and filesystem location utilities
for the Orbit ecosystem.

This package provides a centralized collection of
path-related helpers used throughout Orbit packages,
developer tooling, runtime components, project
generators, and testing infrastructure.

The primary goal of this package is to establish
a consistent approach to path handling across the
entire Orbit ecosystem while reducing duplicated
path resolution logic.

Why This Package Exists
-----------------------
Filesystem paths are a foundational concern across
many Orbit packages.

Examples include:

- Project scaffolding in Orbit CLI.
- Configuration discovery.
- Runtime asset loading.
- Template resolution.
- Build output management.
- Testing infrastructure.
- Workspace detection.

Rather than implementing path handling logic in
multiple locations, Orbit centralizes these
operations within a dedicated package.

Design Goals
------------
The path package is designed around several
core principles:

- Consistency
    Path operations should behave the same way
    throughout the ecosystem.

- Simplicity
    Common path operations should require minimal
    code and provide intuitive APIs.

- Extensibility
    Future project discovery and workspace
    functionality should be implementable without
    breaking existing APIs.

- Maintainability
    Path-related behavior should be easy to locate,
    understand, and evolve.

Future Responsibilities
-----------------------
As Orbit grows, this package may expand to include:

- Project root discovery.
- Workspace resolution.
- Configuration file discovery.
- Template location handling.
- Package root resolution.
- Build artifact management.
- Environment-specific path resolution.

Examples
--------
Retrieve the current project root::

    from orbit_kit.paths import (
        project_root,
    )

    root = project_root()

Retrieve the current working directory::

    from orbit_kit.paths import (
        current_directory,
    )

    cwd = current_directory()

Resolve a filesystem path::

    from orbit_kit.paths import (
        resolve_path,
    )

    path = resolve_path(
        "~/projects/orbit"
    )

Public API
----------
current_directory
    Retrieve the current working directory.

project_root
    Retrieve the active Orbit project root.

resolve_path
    Resolve a path into an absolute filesystem
    location.
"""

from .resolver import (
    current_directory,
    project_root,
    resolve_path,
)

__all__ = [
    "current_directory",
    "project_root",
    "resolve_path",
]
