"""Nox sessions for testing across multiple Python versions."""

import nox

# Python versions to test
PYTHON_VERSIONS = ["3.11", "3.12", "3.13", "3.14"]


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run tests with pytest."""
    # Install package and all dependencies from pyproject.toml
    session.install("-e", ".")
    # Install test dependencies from [dependency-groups]
    session.install("pytest", "pytest-mock", "pytest-cov")
    session.run("pytest", "tests/", "-v")


@nox.session(python=PYTHON_VERSIONS)
def tests_with_coverage(session):
    """Run tests with coverage report."""
    session.install("-e", ".")
    session.install("pytest", "pytest-mock", "pytest-cov")
    session.run(
        "pytest",
        "tests/",
        "-v",
        "--cov=src/parallax",
        "--cov=src/scheduling",
        "--cov-report=term",
        "--cov-report=html",
    )


@nox.session(python="3.12")
def lint(session):
    """Run linting with ruff."""
    session.install("ruff")
    session.run("ruff", "check", ".")


@nox.session(python="3.12")
def format_check(session):
    """Check code formatting with ruff."""
    session.install("ruff")
    session.run("ruff", "format", "--check", ".")
