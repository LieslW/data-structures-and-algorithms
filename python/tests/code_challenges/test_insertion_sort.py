import pytest
from code_challenges.insertion_sort import insertion_sort


def test_exists():
    assert insertion_sort


# @pytest.mark.skip
def test_insertion_sort_list():
    list = [3,5,2,8,6]
    actual = insertion_sort(list)
    expected = [2,3,5,6,8]
    assert actual == expected


# @pytest.mark.skip
def test_insertion_sort_list():
    list = [1,11,13,22,67]
    actual = insertion_sort(list)
    expected = [1,11,13,22,67]
    assert actual == expected

