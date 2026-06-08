"""
Tests for environment detection utilities.

This module validates the runtime environment
detection helpers used throughout the Orbit
ecosystem.
"""

import sys
from pathlib import Path

from orbit_kit.environment import (
    detect_node,
    detect_package_manager,
    python_executable,
)


def test_python_executable_returns_string() -> None:
    """
    Verify the active Python executable is
    returned as a string.
    """

    executable = python_executable()

    assert isinstance(
        executable,
        str,
    )


def test_python_executable_matches_sys_executable() -> None:
    """
    Verify the detected Python executable
    matches the active interpreter.
    """

    assert python_executable() == sys.executable


def test_detect_node_returns_string_or_none() -> None:
    """
    Verify Node.js detection returns a valid
    result type.
    """

    node = detect_node()

    assert node is None or isinstance(node, str)


def test_detect_package_manager_pnpm(
    tmp_path: Path,
) -> None:
    """
    Verify pnpm projects are detected.
    """

    (tmp_path / "pnpm-lock.yaml").touch()

    assert (
        detect_package_manager(
            tmp_path,
        )
        == "pnpm"
    )


def test_detect_package_manager_yarn(
    tmp_path: Path,
) -> None:
    """
    Verify Yarn projects are detected.
    """

    (tmp_path / "yarn.lock").touch()

    assert (
        detect_package_manager(
            tmp_path,
        )
        == "yarn"
    )


def test_detect_package_manager_defaults_to_npm(
    tmp_path: Path,
) -> None:
    """
    Verify npm is used as the default package
    manager when no lockfiles exist.
    """

    assert (
        detect_package_manager(
            tmp_path,
        )
        == "npm"
    )


def test_pnpm_takes_priority_over_yarn(
    tmp_path: Path,
) -> None:
    """
    Verify pnpm has higher detection priority
    than Yarn.
    """

    (tmp_path / "pnpm-lock.yaml").touch()

    (tmp_path / "yarn.lock").touch()

    assert (
        detect_package_manager(
            tmp_path,
        )
        == "pnpm"
    )
