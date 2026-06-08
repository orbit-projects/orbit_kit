"""
orbit_kit.typing.inspection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Typing inspection utilities used throughout the
Orbit ecosystem.

This module provides safe wrappers around common
Python typing operations that are frequently used
by routing, dependency injection, validation,
schema inspection, and framework internals.

The goal of these utilities is to centralize
typing-related logic and provide consistent
behavior across Orbit packages.

Functions
---------
issubclass_safe
    Safely determine subclass relationships.

is_optional_type
    Determine whether a type annotation allows
    None values.

get_annotation_name
    Produce a human-readable annotation name.
"""

from __future__ import annotations

from typing import Any, get_args, get_origin

__all__ = [
    "issubclass_safe",
    "is_optional_type",
    "get_annotation_name",
]


def issubclass_safe(
    cls: Any,
    base: type,
) -> bool:
    """
    Safely determine whether an object is a subclass
    of another type.

    This helper protects framework internals from
    ``TypeError`` exceptions that occur when
    ``issubclass`` is called with non-class objects.

    Parameters
    ----------
    cls:
        Object to inspect.

    base:
        Base class reference.

    Returns
    -------
    bool
        True if a valid subclass relationship exists,
        otherwise False.

    Examples
    --------
    Standard usage::

        issubclass_safe(
            ValueError,
            Exception,
        )

    Invalid input::

        issubclass_safe(
            "hello",
            Exception,
        )
    """

    try:
        return issubclass(cls, base)
    except TypeError:
        return False


def is_optional_type(
    annotation: Any,
) -> bool:
    """
    Determine whether a type annotation allows
    ``None`` values.

    Supports:

    - Optional[str]
    - Union[str, None]
    - str | None

    Parameters
    ----------
    annotation:
        Type annotation to inspect.

    Returns
    -------
    bool
        True if the annotation accepts None.
    """

    origin = get_origin(annotation)

    if origin is None:
        return False

    return type(None) in get_args(annotation)


def get_annotation_name(
    annotation: Any,
) -> str:
    """
    Retrieve a human-readable annotation name.

    This helper is primarily intended for
    diagnostics, debugging, logging, and
    developer-facing error messages.

    Parameters
    ----------
    annotation:
        Type annotation to inspect.

    Returns
    -------
    str
        Human-readable annotation name.
    """

    name = getattr(
        annotation,
        "__name__",
        None,
    )

    if name is not None:
        return name

    return str(annotation)
