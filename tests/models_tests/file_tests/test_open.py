from collections import abc

import pytest
from hypothesis import given

from rsrc_local.models import File
from tests import strategies


@given(strategies.existent_files, strategies.booleans)
def test_basic(file: File, binary_mode: bool) -> None:
    result = file.open(binary_mode=binary_mode)

    assert isinstance(result, abc.Iterable)
    assert all(isinstance(line, bytes if binary_mode else str)
               for line in result)


@given(strategies.non_existent_files)
def test_non_existent_file(file: File) -> None:
    with pytest.raises(OSError):
        file.open()
