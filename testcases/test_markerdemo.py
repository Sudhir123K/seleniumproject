import pytest

@pytest.mark.functional #we can use multi marker for one function
@pytest.mark.regression
def test_login_brow():
    print("login is working")
    assert 5 == 5

@pytest.mark.xfail      #it is used when we already know tets case will fail
def test_login_brow1():
        print("login is working")
        assert 6 == 5

@pytest.mark.sanity
def test_login_brow2():
    print("login is working")
    assert 8 == 8