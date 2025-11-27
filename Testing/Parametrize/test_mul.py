import pytest
from mul import multiply
@pytest.mark.parametrize("a,b,expected",[
    (1,2,2),
    (3,4,12),
    (0,3,0),
    (-2,4,-6)])
def test_muliply(a,b,expected):
    assert multiply(a,b)==expected