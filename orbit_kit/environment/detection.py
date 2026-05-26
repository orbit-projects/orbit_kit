"""
Environment Detection Utilities

Provides shared runtime environment
detection helpers.
"""

from pathlib import Path
import shutil
import sys


def detect_python() -> str:
    """
    Retrieve active Python executable.

    Returns:
        Active Python executable path.
    """

    return sys.executable


def detect_node() -> str | None:
    """
    Detect Node.js runtime.

    Returns:
        Node.js executable path.
    """

    return shutil.which("node")


def detect_package_manager(
    directory: Path,
) -> str:
    """
    Detect frontend package manager.

    Detection priority:
    - pnpm
    - yarn
    - npm

    Args:
        directory:
            Project directory.

    Returns:
        Detected package manager.
    """

    if (directory / "pnpm-lock.yaml").exists():
        return "pnpm"

    if (directory / "yarn.lock").exists():
        return "yarn"

    return "npm"
