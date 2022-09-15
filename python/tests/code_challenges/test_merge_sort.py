import pytest
from code_challenges.merge_sort import merge_sort


def merge_sort_exists():
    assert merge_sort


# @pytest.mark.skip
def test_base_case():
    list = [4,3,6,7,5,12]
    actual = merge_sort(list)
    expected = [3,4,5,6,7,12]
    assert actual == expected


# @pytest.mark.skip
def test_already_sorted():
    list = [1,2,3,4,5,6]
    actual = merge_sort(list)
    expected = [1,2,3,4,5,6]
    assert actual == expected


# @pytest.mark.skip
def test_in_reverse():
    list = [6,5,4,3,2,1]
    actual = merge_sort(list)
    expected = [1,2,3,4,5,6]
    assert actual == expected


# @pytest.mark.skip
def test_duplicates():
    arr = [3,1,2,3,2,3]
    actual = merge_sort(arr)
    expected = [1,2,2,3,3,3]
    assert actual == expected


# @pytest.mark.skip
def test_same_numbers():
    arr = [7,7,7,7,7,7,7,7,7,7]
    actual = merge_sort(arr)
    expected = [7,7,7,7,7,7,7,7,7,7]
    assert actual == expected


# @pytest.mark.skip
def test_negative_numbers():
    arr = [-1,-2,-3,-4,-5,-6]
    actual = merge_sort(arr)
    expected = [-6,-5,-4,-3,-2,-1]
    assert actual == expected
