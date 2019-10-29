import pytest
from hypothesis import given

from rsrc_local.models import (Directory,
                               File)
from tests import strategies


@given(strategies.existent_files)
def test_same_file(file: File) -> None:
    with pytest.raises(OSError):
        file.receive(file)


@given(strategies.existent_files, strategies.non_existent_files)
def test_non_existent_destination(existent_file: File,
                                  non_existent_file: File) -> None:
    non_existent_file.receive(existent_file)

    assert non_existent_file.exists()


@given(strategies.existent_files, strategies.non_existent_files)
def test_non_existent_source(existent_file: File,
                             non_existent_file: File) -> None:
    with pytest.raises(OSError):
        existent_file.receive(non_existent_file)


@given(strategies.existent_files, strategies.existent_directories)
def test_non_stream_source(existent_file: File,
                           directory: Directory) -> None:
    with pytest.raises(TypeError):
        existent_file.receive(directory)
