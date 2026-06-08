"""
Orbit Kit Test Configuration

Shared pytest configuration and fixtures for the
Orbit Kit test suite.

This module serves as the local test integration
layer for Orbit Kit.

As the Orbit ecosystem evolves, common fixtures,
assertions, factories, and testing utilities may
be migrated into a dedicated shared testing package
while keeping package-specific fixtures within
individual test suites.

Current Responsibilities
------------------------
- Shared Orbit Kit fixtures.
- Package-level pytest configuration.
- Future integration with Orbit Testing.

Testing Philosophy
------------------
Orbit follows a hybrid testing architecture:

- Shared testing infrastructure is centralized
  within a common testing package.

- Package-specific tests remain colocated with
  their respective packages.

This approach improves consistency while allowing
individual packages to maintain focused and
independent test suites.
"""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture
def project_root() -> Path:
    """
    Retrieve the Orbit Kit project root.

    Returns
    -------
    Path
        Repository root directory.
    """

    return Path(__file__).parent.parent
