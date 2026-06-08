"""
Tests for runtime metadata models.

This module validates the runtime information
models used throughout the Orbit ecosystem.
"""

from dataclasses import FrozenInstanceError

import pytest

from orbit_kit.runtime import (
    RuntimeInfo,
)


def test_runtime_info_creation() -> None:
    """
    Verify RuntimeInfo instances can be created.
    """

    runtime = RuntimeInfo(
        framework="orbit",
        framework_version="0.1.0",
        runtime="cpython",
        environment="development",
        python_version="3.12",
        platform="linux",
    )

    assert isinstance(
        runtime,
        RuntimeInfo,
    )


def test_runtime_info_fields() -> None:
    """
    Verify runtime metadata fields are stored
    correctly.
    """

    runtime = RuntimeInfo(
        framework="orbit",
        framework_version="0.1.0",
        runtime="cpython",
        environment="development",
        python_version="3.12",
        platform="linux",
    )

    assert runtime.framework == "orbit"

    assert runtime.framework_version == "0.1.0"

    assert runtime.runtime == "cpython"

    assert runtime.environment == "development"

    assert runtime.python_version == "3.12"

    assert runtime.platform == "linux"


def test_runtime_info_repr() -> None:
    """
    Verify dataclass representation contains
    useful metadata.
    """

    runtime = RuntimeInfo(
        framework="orbit",
        framework_version="0.1.0",
        runtime="cpython",
        environment="development",
        python_version="3.12",
        platform="linux",
    )

    representation = repr(
        runtime,
    )

    assert "RuntimeInfo" in representation

    assert "orbit" in representation


def test_runtime_info_is_immutable() -> None:
    """
    Verify frozen runtime models cannot be
    modified.
    """

    runtime = RuntimeInfo(
        framework="orbit",
        framework_version="0.1.0",
        runtime="cpython",
        environment="development",
        python_version="3.12",
        platform="linux",
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        runtime.framework = "modified"
