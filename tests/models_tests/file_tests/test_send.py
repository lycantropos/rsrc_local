import pytest
from hypothesis import given

from rsrc_local.models import (Directory,
                               File)
from tests import strategies


@given(strategies.existent_files)
def test_same_file(file: File) -> None:
    with pytest.raises(OSError):
        file.send(file)


@given(strategies.existent_files, strategies.non_existent_files)
def test_non_existent_destination(existent_file: File,
                                  non_existent_file: File) -> None:
    existent_file.send(non_existent_file)

    assert non_existent_file.exists()


@given(strategies.existent_files, strategies.non_existent_files)
def test_non_existent_source(existent_file: File,
                             non_existent_file: File) -> None:
    with pytest.raises(OSError):
        non_existent_file.send(existent_file)


@given(strategies.existent_files, strategies.existent_directories)
def test_non_stream_destination(existent_file: File,
                                directory: Directory) -> None:
    with pytest.raises(TypeError):
        existent_file.send(directory)
