import pytest
from hypothesis import given
from rsrc.models import Base

from rsrc_local.models import Directory
from tests import strategies


@given(strategies.non_empty_directories)
def test_basic(directory: Directory) -> None:
    assert all(isinstance(child, Base)
               for child in directory)


@given(strategies.non_empty_directories)
def test_all_children_exist(directory: Directory) -> None:
    assert all(child.exists()
               for child in directory)


@given(strategies.non_empty_directories)
def test_all_children_unique(directory: Directory) -> None:
    children = list(directory)

    assert all(children.count(child) == 1
               for child in directory)


@given(strategies.non_existent_directories)
def test_non_existent_directory(directory: Directory) -> None:
    with pytest.raises(OSError):
        list(directory)
