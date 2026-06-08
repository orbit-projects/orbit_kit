"""
orbit_kit.runtime
~~~~~~~~~~~~~~~~~

Runtime metadata abstractions used throughout the
Orbit ecosystem.

This package provides strongly typed runtime models
that describe the active execution environment.

Runtime information is commonly used by:

- Orbit CLI
- Orbit Core
- Orbit Server
- Diagnostics tooling
- Environment inspection
- Testing infrastructure

The package exists to provide a stable and
consistent representation of runtime metadata
throughout the ecosystem.

Examples
--------
Create runtime metadata::

    from orbit_kit.runtime import (
        RuntimeInfo,
    )

    runtime = RuntimeInfo(
        framework="orbit",
        framework_version="1.0.0",
        runtime="cpython",
        environment="development",
        python_version="3.13.0",
        platform="linux",
    )

Public API
----------
RuntimeInfo
    Runtime metadata container.
"""

from .models import RuntimeInfo

__all__ = [
    "RuntimeInfo",
]
