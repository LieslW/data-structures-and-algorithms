import pytest
from code_challenges.insertion_sort import InsertionSort


def test_exists():
    assert InsertionSort


@pytest.mark.skip
def test_append():
    insertion_sort = InsertionSort()

    insertion_sort.insert("")

    assert str(insertion_sort) == "{ banana } -> { apple } -> { cucumber } -> NULL"
