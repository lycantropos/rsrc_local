from hypothesis import given
from rsrc.models import Resource

from tests import strategies


@given(strategies.resources)
def test_round_trip(resource: Resource) -> None:
    result = str(resource)

    assert resource.from_string(result) == resource
