"""
orbit_kit.filesystem
~~~~~~~~~~~~~~~~~~~~

Filesystem utilities used throughout the Orbit
ecosystem.

This package provides a centralized collection of
filesystem operations that are shared across Orbit
packages and developer tooling.

Rather than interacting directly with low-level
filesystem APIs throughout the codebase, Orbit
components should use these utilities to ensure
consistent behavior, error handling, and developer
experience.

Features
--------
- Directory creation
- Directory removal
- Directory copying
- File reading
- File writing
- Path existence checks

Design Goals
------------
The filesystem package exists to:

- Reduce duplicated filesystem logic.
- Provide consistent exception handling.
- Expose a stable public API.
- Improve maintainability across Orbit packages.
- Simplify testing through centralized operations.

Error Handling
--------------
Filesystem operations normalize underlying Python
filesystem exceptions into Orbit-specific exceptions.

This allows Orbit applications and internal
components to catch predictable exception types
without depending on implementation details of
the standard library.

Examples
--------
Create a directory::

    from orbit_kit.filesystem import (
        ensure_directory,
    )

    ensure_directory("build")

Read a file::

    from orbit_kit.filesystem import (
        read_file,
    )

    content = read_file(
        "config.toml",
    )

Write a file::

    from orbit_kit.filesystem import (
        write_file,
    )

    write_file(
        "output.txt",
        "Hello Orbit",
    )

Check path existence::

    from orbit_kit.filesystem import (
        path_exists,
    )

    if path_exists("README.md"):
        ...
"""

from .operations import (
    copy_directory,
    ensure_directory,
    path_exists,
    read_file,
    remove_directory,
    write_file,
)

__all__ = [
    "ensure_directory",
    "remove_directory",
    "copy_directory",
    "read_file",
    "write_file",
    "path_exists",
]
