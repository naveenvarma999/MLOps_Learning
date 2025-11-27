import pytest
from add_sum import add
@pytest.mark.parametrize("a,b,result",[
    (1,2,3),
    (4,5,9),
    (5,6,11),
    (3,4,7),
    (3,3,6)
])
def test_sum(a,b,result):
    assert add(a,b) == result