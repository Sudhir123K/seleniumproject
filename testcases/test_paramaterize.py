import pytest


@pytest.mark.parametrize("name, role",[("ram", "QA"),("ravi","developer")])
def test_data(name, role):
    assert name != None
    assert role != None

@pytest.fixture(scope="module", params=["www.amazone.com","www.google.com"])
def val(request):
    return request.param

def test_val1(val):
    assert val != None
