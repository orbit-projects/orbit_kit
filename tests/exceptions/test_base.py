"""
Tests for Orbit Kit exceptions.

This module verifies the behavior of the shared
Orbit Kit exception hierarchy.

The exception hierarchy serves as the foundation
for error handling throughout the package and
therefore requires comprehensive validation.
"""

from orbit_kit.exceptions import (
    ConsoleError,
    EnvironmentError,
    FilesystemError,
    OrbitKitError,
    PathError,
    ProcessError,
    RuntimeEnvironmentError,
    ValidationError,
)


def test_orbit_kit_error_default_message() -> None:
    """
    Verify the default OrbitKitError message.
    """

    error = OrbitKitError()

    assert str(error) == "An Orbit Kit error occurred."


def test_orbit_kit_error_custom_message() -> None:
    """
    Verify custom exception messages.
    """

    error = OrbitKitError("Custom error message.")

    assert str(error) == "Custom error message."


def test_validation_error_default_message() -> None:
    """
    Verify ValidationError default message.
    """

    error = ValidationError()

    assert str(error) == "Validation failed."


def test_process_error_default_message() -> None:
    """
    Verify ProcessError default message.
    """

    error = ProcessError()

    assert str(error) == "Process execution failed."


def test_filesystem_error_default_message() -> None:
    """
    Verify FilesystemError default message.
    """

    error = FilesystemError()

    assert str(error) == "Filesystem operation failed."


def test_path_error_default_message() -> None:
    """
    Verify PathError default message.
    """

    error = PathError()

    assert str(error) == "Path operation failed."


def test_environment_error_default_message() -> None:
    """
    Verify EnvironmentError default message.
    """

    error = EnvironmentError()

    assert str(error) == "Environment operation failed."


def test_runtime_environment_error_default_message() -> None:
    """
    Verify RuntimeEnvironmentError default
    message.
    """

    error = RuntimeEnvironmentError()

    assert str(error) == "Runtime inspection failed."


def test_console_error_default_message() -> None:
    """
    Verify ConsoleError default message.
    """

    error = ConsoleError()

    assert str(error) == "Console operation failed."


def test_validation_error_inherits_orbit_kit_error() -> None:
    """
    Verify ValidationError inherits from
    OrbitKitError.
    """

    error = ValidationError()

    assert isinstance(
        error,
        OrbitKitError,
    )


def test_process_error_inherits_orbit_kit_error() -> None:
    """
    Verify ProcessError inherits from
    OrbitKitError.
    """

    error = ProcessError()

    assert isinstance(
        error,
        OrbitKitError,
    )
