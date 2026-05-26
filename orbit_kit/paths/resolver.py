"""
Path Resolution Utilities

Shared filesystem path helpers
used throughout Orbit.
"""

from pathlib import Path


def project_root() -> Path:
    """
    Retrieve current project root.

    Returns:
        Current working directory.
    """

    return Path.cwd()
