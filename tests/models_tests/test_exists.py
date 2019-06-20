import os
import shutil

import pytest
from hypothesis import given
from rsrc.base import deserialize

from rsrc_local.models import (Directory,
                               File)
from tests import strategies
from tests.utils import (implication,
                         touch)


@given(strategies.existent_files)
def test_existent_file(file: File) -> None:
    assert file.exists()


@given(strategies.non_existent_files)
def test_non_existent_file(file: File) -> None:
    assert not file.exists()


@given(strategies.existent_directories)
def test_removing_directory(directory: Directory) -> None:
    path_string = str(directory)

    shutil.rmtree(path_string)

    assert not directory.exists()


@given(strategies.non_existent_files)
def test_creating_directory_with_same_name(file: File) -> None:
    path_string = str(file)

    os.mkdir(path_string)

    with pytest.raises(OSError):
        file.exists()


@given(strategies.non_existent_directories)
def test_creating_file_with_same_name(directory: Directory) -> None:
    path_string = str(directory)

    touch(path_string)

    with pytest.raises(OSError):
        directory.exists()


@given(strategies.paths_strings)
def test_connection_with_deserialize(string: str) -> None:
    result = deserialize(string)

    assert implication(not result.exists(), not isinstance(result, Directory))
