from hypothesis import given
from rsrc.models import (Resource,
                         URL)

from rsrc_local.base import deserialize_url
from tests import strategies


@given(strategies.resources)
def test_basic(resource: Resource) -> None:
    assert isinstance(resource.url, URL)


@given(strategies.existent_resources)
def test_round_trip(resource: Resource) -> None:
    assert deserialize_url(str(resource.url)) == resource
