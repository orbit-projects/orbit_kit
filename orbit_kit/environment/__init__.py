"""
Orbit Environment Utilities

Shared environment detection helpers
used throughout the Orbit ecosystem.

Exports:
    detect_python:
        Detect Python runtime.

    detect_node:
        Detect Node.js runtime.

    detect_package_manager:
        Detect frontend package manager.
"""

from .detection import (
    detect_node,
    detect_package_manager,
    detect_python,
)

__all__ = [
    "detect_python",
    "detect_node",
    "detect_package_manager",
]
