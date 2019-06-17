import pytest
from hypothesis import given

from rsrc_local.models import File
from tests import strategies


@given(strategies.existent_directories_paths_strings)
def test_existent_directory_path_string(path_string: str) -> None:
    with pytest.raises(ValueError):
        File.from_string(path_string)
