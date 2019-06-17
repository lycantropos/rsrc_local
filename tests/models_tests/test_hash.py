from hypothesis import given
from rsrc.models import Resource

from tests import strategies
from tests.utils import equivalence


@given(strategies.resources)
def test_basic(resource: Resource) -> None:
    result = hash(resource)

    assert isinstance(result, int)


@given(strategies.resources)
def test_determinism(resource: Resource) -> None:
    result = hash(resource)

    assert result == hash(resource)


@given(strategies.resources, strategies.resources)
def test_connection_with_equality(left_resource: Resource,
                                  right_resource: Resource) -> None:
    assert equivalence(left_resource == right_resource,
                       hash(left_resource) == hash(right_resource))
