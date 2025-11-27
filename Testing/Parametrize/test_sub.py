import pytest 
from sub import sub
@pytest.mark.parametrize("a,b,result",[
    (4,3,1),
    (6,7,-1),
    (4,1,3),
    (7,2,5),
    (8,6,2)])
def test_subdata(a,b,result):
    assert sub(a,b)==result