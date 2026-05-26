"""
Runtime Models

Shared runtime metadata abstractions.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class RuntimeInfo:
    """
    Shared runtime metadata model.
    """

    framework: str
    runtime: str
    environment: str
