import pytest
import count

def test_count_zeros():
    assert count.count([0,0,0], 0) == 3

def test_count_string():
    assert count.count(["a","a","a"], "a") == 3

#type 'pytest' in terminal to go through the tests (within the directory)