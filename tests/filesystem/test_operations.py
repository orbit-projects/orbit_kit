"""
Tests for filesystem operations.

This module validates the filesystem utilities
used throughout the Orbit ecosystem.
"""

from pathlib import Path

from orbit_kit.filesystem import (
    copy_directory,
    ensure_directory,
    path_exists,
    read_file,
    remove_directory,
    write_file,
)


def test_ensure_directory_creates_directory(
    tmp_path: Path,
) -> None:
    """
    Verify directories are created when missing.
    """

    directory = tmp_path / "orbit"

    ensure_directory(
        directory,
    )

    assert directory.exists()
    assert directory.is_dir()


def test_remove_directory_removes_directory(
    tmp_path: Path,
) -> None:
    """
    Verify directories are removed recursively.
    """

    directory = tmp_path / "orbit"

    directory.mkdir()

    remove_directory(
        directory,
    )

    assert not directory.exists()


def test_copy_directory_copies_contents(
    tmp_path: Path,
) -> None:
    """
    Verify directory trees are copied.
    """

    source = tmp_path / "source"
    destination = tmp_path / "destination"

    source.mkdir()

    file_path = source / "test.txt"

    file_path.write_text(
        "orbit",
        encoding="utf-8",
    )

    copy_directory(
        source,
        destination,
    )

    copied_file = destination / "test.txt"

    assert copied_file.exists()

    assert (
        copied_file.read_text(
            encoding="utf-8",
        )
        == "orbit"
    )


def test_write_file_creates_file(
    tmp_path: Path,
) -> None:
    """
    Verify files can be written.
    """

    file_path = tmp_path / "test.txt"

    write_file(
        file_path,
        "orbit",
    )

    assert file_path.exists()


def test_read_file_returns_content(
    tmp_path: Path,
) -> None:
    """
    Verify file contents are read correctly.
    """

    file_path = tmp_path / "test.txt"

    file_path.write_text(
        "orbit",
        encoding="utf-8",
    )

    assert (
        read_file(
            file_path,
        )
        == "orbit"
    )


def test_write_and_read_file_roundtrip(
    tmp_path: Path,
) -> None:
    """
    Verify content survives a write/read cycle.
    """

    file_path = tmp_path / "roundtrip.txt"

    write_file(
        file_path,
        "hello orbit",
    )

    content = read_file(
        file_path,
    )

    assert content == "hello orbit"


def test_path_exists_for_existing_path(
    tmp_path: Path,
) -> None:
    """
    Verify existing paths return True.
    """

    assert path_exists(
        tmp_path,
    )


def test_path_exists_for_missing_path(
    tmp_path: Path,
) -> None:
    """
    Verify missing paths return False.
    """

    missing = tmp_path / "missing"

    assert not path_exists(
        missing,
    )
