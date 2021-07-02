import pytest
from demoproject.custom_utils import add

def test_add():
    assert add(2,5) == 7
    assert add(2.5,2.5) == 5