"""
Tests for Orbit typing inspection utilities.

This module validates the behavior of the shared
typing helpers used throughout the Orbit ecosystem.
"""

from orbit_kit.typing import (
    get_annotation_name,
    is_optional_type,
    issubclass_safe,
)


def test_issubclass_safe_with_valid_subclass() -> None:
    """
    Verify subclass relationships are detected
    correctly.
    """

    assert issubclass_safe(
        ValueError,
        Exception,
    )


def test_issubclass_safe_with_invalid_subclass() -> None:
    """
    Verify unrelated types return False.
    """

    assert not issubclass_safe(
        str,
        Exception,
    )


def test_issubclass_safe_with_non_class_object() -> None:
    """
    Verify non-class objects do not raise errors.
    """

    assert not issubclass_safe(
        "orbit",
        Exception,
    )


def test_issubclass_safe_with_none() -> None:
    """
    Verify None returns False.
    """

    assert not issubclass_safe(
        None,
        Exception,
    )


def test_is_optional_type_with_optional_union() -> None:
    """
    Verify modern optional annotations are
    detected correctly.
    """

    assert is_optional_type(
        str | None,
    )


def test_is_optional_type_with_standard_type() -> None:
    """
    Verify non-optional annotations return False.
    """

    assert not is_optional_type(
        str,
    )


def test_is_optional_type_with_integer_type() -> None:
    """
    Verify primitive types are not treated as
    optional.
    """

    assert not is_optional_type(
        int,
    )


def test_get_annotation_name_for_builtin_type() -> None:
    """
    Verify builtin type names are returned.
    """

    assert get_annotation_name(str) == "str"


def test_get_annotation_name_for_custom_type() -> None:
    """
    Verify custom type names are returned.
    """

    class OrbitType:
        pass

    assert (
        get_annotation_name(
            OrbitType,
        )
        == "OrbitType"
    )


def test_get_annotation_name_for_generic_annotation() -> None:
    """
    Verify generic annotations return a string
    representation.
    """

    result = get_annotation_name(
        list[str],
    )

    assert isinstance(
        result,
        str,
    )
