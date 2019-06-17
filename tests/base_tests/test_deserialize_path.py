from hypothesis import given
from rsrc.models import Base

from rsrc_local.base import deserialize_path
from rsrc_local.models import (Directory,
                               File)
from tests import strategies


@given(strategies.paths_strings)
def test_basic(string: str) -> None:
    result = deserialize_path(string)

    assert isinstance(result, Base)


@given(strategies.existent_directories_paths_strings)
def test_directory_path_string(string: str) -> None:
    result = deserialize_path(string)

    assert isinstance(result, Directory)


@given(strategies.files_paths_strings)
def test_file_path_string(string: str) -> None:
    result = deserialize_path(string)

    assert isinstance(result, File)
