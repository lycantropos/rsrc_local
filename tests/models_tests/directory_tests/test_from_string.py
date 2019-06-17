import pytest
from hypothesis import given

from rsrc_local.models import Directory
from tests import strategies


@given(strategies.existent_files_paths_strings)
def test_existent_file_path_string(path_string: str) -> None:
    with pytest.raises(ValueError):
        Directory.from_string(path_string)
