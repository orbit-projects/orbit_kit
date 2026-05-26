"""
Orbit Kit Package

Shared developer infrastructure and reusable
framework utilities used throughout the Orbit ecosystem.

This package provides:

- Filesystem utilities
- Process management utilities
- Runtime helpers
- Validation utilities
- Environment detection
- Shared developer tooling abstractions

Orbit Kit is intended to serve as the foundational
tooling layer for all Orbit ecosystem packages.

Exports:
    console:
        Terminal and console utilities.

    filesystem:
        Shared filesystem utilities.

    process:
        Shared subprocess and runtime utilities.

    validation:
        Shared validation helpers.

    environment:
        Environment detection utilities.
"""

__all__ = [
    "console",
    "filesystem",
    "process",
    "validation",
    "environment",
]
