"""
Orbit Exception Hierarchy

Provides shared exception abstractions
for Orbit ecosystem packages.
"""


class OrbitKitError(Exception):
    """
    Base Orbit Kit exception.
    """


class ValidationError(
    OrbitKitError,
):
    """
    Raised during validation failures.
    """


class ProcessError(
    OrbitKitError,
):
    """
    Raised during process execution failures.
    """
