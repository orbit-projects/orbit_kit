"""
orbit_kit.typing
~~~~~~~~~~~~~~~~

Shared typing utilities used throughout the
Orbit ecosystem.

This package centralizes common typing helpers,
annotation inspection utilities, and reusable
typing infrastructure used across Orbit
packages.

The goal of this package is to provide a single
location for typing-related functionality and
avoid duplicating type inspection logic across
the ecosystem.

Examples
--------
Inspect an annotation::

    from orbit_kit.typing import (
        is_optional_type,
    )

    is_optional_type(str | None)

Safely inspect subclass relationships::

    from orbit_kit.typing import (
        issubclass_safe,
    )

    issubclass_safe(
        ValueError,
        Exception,
    )
"""

from .inspection import (
    get_annotation_name,
    is_optional_type,
    issubclass_safe,
)

__all__ = [
    "issubclass_safe",
    "is_optional_type",
    "get_annotation_name",
]
