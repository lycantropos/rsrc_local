from hypothesis import given

from rsrc_local.models import Directory
from tests import strategies


@given(strategies.non_empty_directories)
def test_children_construction(directory: Directory) -> None:
    assert all(directory.join(child.url.path.name) == child
               for child in directory)
