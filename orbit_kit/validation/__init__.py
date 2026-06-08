"""
orbit_kit.validation
~~~~~~~~~~~~~~~~~~~~

Validation utilities used throughout the Orbit
ecosystem.

This package provides reusable validation helpers
that are shared across Orbit packages, tooling,
runtime components, project generators, and test
infrastructure.

The primary goal of the validation package is to
centralize common validation logic and provide
consistent error reporting throughout the
ecosystem.

Why This Package Exists
-----------------------
Validation logic often becomes duplicated across
large projects.

Orbit centralizes common validation behavior to:

- Improve consistency.
- Reduce code duplication.
- Standardize exception handling.
- Simplify testing.
- Improve maintainability.

Current Responsibilities
------------------------
The package currently provides validation helpers
for filesystem resources.

Examples include:

- File validation.
- Directory validation.
- Path existence validation.

Future versions may expand to support:

- Configuration validation.
- Runtime validation.
- Environment validation.
- Dependency validation.
- Project structure validation.

Examples
--------
Validate a directory::

    from orbit_kit.validation import (
        validate_directory,
    )

    validate_directory(
        "src"
    )

Validate a file::

    from orbit_kit.validation import (
        validate_file,
    )

    validate_file(
        "pyproject.toml"
    )

Validate path existence::

    from orbit_kit.validation import (
        validate_exists,
    )

    validate_exists(
        ".git"
    )

Public API
----------
validate_exists
    Validate path existence.

validate_directory
    Validate directory existence.

validate_file
    Validate file existence.
"""

from .filesystem import (
    validate_directory,
    validate_exists,
    validate_file,
)

__all__ = [
    "validate_exists",
    "validate_directory",
    "validate_file",
]
