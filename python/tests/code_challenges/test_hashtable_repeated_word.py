import pytest
from code_challenges.hashtable_repeated_word import hashtable_repeated_word


# @pytest.mark.skip("TODO")
def test_blank():
    actual = hashtable_repeated_word("")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_no_repeat():
    actual = hashtable_repeated_word("We all float down here")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_same_words():
    actual = hashtable_repeated_word("cat cat")
    expected = "cat"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_repeated_word():
    actual = hashtable_repeated_word("cat dog cat")
    expected = "cat"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_first_repeated_word():
    actual = hashtable_repeated_word("cat dog cat dog")
    expected = "cat"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_first_repeated_word_2():
    actual = hashtable_repeated_word("cat dog dog cat")
    expected = "dog"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_case():
    actual = hashtable_repeated_word("cat dog DOG cat")
    expected = "dog"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_case_flipped():
    actual = hashtable_repeated_word("cat DOG dog cat")
    expected = "dog"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_punctuation():
    actual = hashtable_repeated_word("cat? dog! dog, cat.")
    expected = "dog"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_punctuation_joins():
    txt = """
  cat
  cat.cat-cat
  dog
  cat?cat
  dog
  """

    actual = hashtable_repeated_word(txt)
    expected = "dog"
    assert actual == expected
