"""
orbit_kit.runtime.models
~~~~~~~~~~~~~~~~~~~~~~~~

Runtime metadata models used throughout the
Orbit ecosystem.

This module provides structured runtime information
that can be consumed by framework components,
developer tooling, diagnostics systems, testing
infrastructure, and operational utilities.

The primary goal of these models is to provide a
consistent representation of runtime state without
requiring individual Orbit packages to gather and
manage environment information independently.

Why This Module Exists
----------------------
As the Orbit ecosystem grows, multiple packages
will require access to runtime information.

Examples include:

- Orbit CLI diagnostics.
- Environment inspection commands.
- Framework startup reporting.
- Debugging utilities.
- Development tooling.
- Test infrastructure.
- Error reporting.
- System compatibility checks.

Rather than exposing loosely structured dictionaries,
Orbit uses dedicated runtime models to provide
consistent and type-safe metadata handling.

Design Goals
------------
The runtime models are designed around several
principles:

- Consistency
    Runtime metadata should be represented in a
    predictable format throughout the ecosystem.

- Type Safety
    Runtime information should be strongly typed
    and easy to reason about.

- Diagnostics
    Models should contain sufficient information
    to support troubleshooting and environment
    inspection.

- Extensibility
    Additional metadata fields should be easy to
    introduce without requiring significant
    architectural changes.

Example
-------
Create runtime metadata::

    runtime = RuntimeInfo(
        framework="orbit",
        framework_version="1.0.0",
        runtime="cpython",
        environment="development",
        python_version="3.13.0",
        platform="linux",
    )

Access metadata::

    print(runtime.python_version)

Future Responsibilities
-----------------------
Future versions of Orbit may extend these models
to support:

- Build metadata.
- Git metadata.
- Workspace metadata.
- Runtime capabilities.
- Installed package information.
- Deployment metadata.
- Environment diagnostics.
"""

from __future__ import annotations

from dataclasses import dataclass

__all__ = [
    "RuntimeInfo",
]


@dataclass(
    slots=True,
    frozen=True,
)
class RuntimeInfo:
    """
    Runtime metadata container.

    This model provides a normalized representation
    of the active execution environment.

    Runtime information can be consumed by Orbit
    packages, tooling, diagnostics systems, and
    operational utilities.

    Attributes
    ----------
    framework:
        Framework name.

        Examples
        --------
        - orbit
        - orbit-server

    framework_version:
        Active framework version.

    runtime:
        Runtime implementation.

        Examples
        --------
        - cpython
        - pypy

    environment:
        Active execution environment.

        Examples
        --------
        - development
        - testing
        - staging
        - production

    python_version:
        Active Python version.

    platform:
        Operating system platform.

        Examples
        --------
        - linux
        - windows
        - darwin
    """

    #: Framework name.
    framework: str

    #: Framework version.
    framework_version: str

    #: Runtime implementation.
    runtime: str

    #: Active environment.
    environment: str

    #: Python version.
    python_version: str

    #: Operating system platform.
    platform: str
