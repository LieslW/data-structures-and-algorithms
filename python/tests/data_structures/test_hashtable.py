import pytest
from data_structures.hashtable import Hashtable


"""
[X] Setting a key/value to your hashtable results in the value being in the data structure
[] Retrieving based on a key returns the value stored
[X] Successfully returns null for a key that does not exist in the hashtable
[] Successfully returns a list of all unique keys that exist in the hashtable
[] Successfully handle a collision within the hashtable
[] Successfully retrieve a value from a bucket within the hashtable that has a collision
[X] Successfully hash a key to an in-range value
"""


def test_exists():
    assert Hashtable


# @pytest.mark.skip
def test_get_returns_none_for_the_missing_key():
    table = Hashtable()
    actual = table.get("spam")
    expected = None
    assert actual == expected


# @pytest.mark.skip
def tests_buckets_size():
    table = Hashtable()
    actual = len(table.buckets)
    expected = 1024
    assert actual == expected


# @pytest.mark.skip
def test_hash_in_range():
    table = Hashtable(size=2)
    keys = ["spam", "eggs", "bacon", "OJ", "toast"]
    for key in keys:
        index = table.hash(key)
        assert 0 <= index < table.size


# @pytest.mark.skip
def test_set_does_not_blow_up():
    table = Hashtable()
    table.set("eggs", "bacon")
    assert True


# @pytest.mark.skip
def test_contains():
    table = Hashtable()
    table.set("eggs", "bacon")
    actual = table.contains("eggs")
    expected = True
    assert actual == expected


# @pytest.mark.skip
def test_not_contains():
    table = Hashtable()
    table.set("eggs", "bacon")
    actual = table.contains("spam")
    expected = False
    assert actual == expected


# @pytest.mark.skip
def test_keys():
    table = Hashtable()
    table.set("eggs", "bacon")
    table.set("OJ", "spam")
    keys = table.keys()
    actual = sorted(keys)
    expected = ["OJ", "eggs"]
    assert actual == expected



# @pytest.mark.skip("TODO")
# def test_get_apple():
#     hashtable = Hashtable()
#     hashtable.set("apple", "Used for apple sauce")
#     actual = hashtable.get("apple")
#     expected = "Used for apple sauce"
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_internals():
#     hashtable = Hashtable(1024)
#     hashtable.set("ahmad", 30)
#     hashtable.set("silent", True)
#     hashtable.set("listen", "to me")
#
#     actual = []
#
#     # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
#     for item in hashtable._buckets:
#         if item:
#             actual.append(item.display())
#
#     expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]
#
#     assert actual == expected
