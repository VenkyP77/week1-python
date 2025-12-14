import pytest
from textutils import cleaner, analysis


# 1. Test the "Happy Path" (Does it work with normal input?)
def test_remove_special_chars_simple():
    raw = "Hello World!"
    expected = "Hello World"  # Exclamation removed
    assert cleaner.remove_special_chars(raw) == expected


# 2. Test "Edge Cases" (What happens with weird input?)
def test_remove_special_chars_empty():
    assert cleaner.remove_special_chars("") == ""


def test_remove_special_chars_numbers():
    # Should keep numbers, remove symbols
    raw = "User123 #$%"
    expected = "User123 "
    assert cleaner.remove_special_chars(raw) == expected


# 3. Test the Analysis module
def test_count_words():
    text = "Python is amazing"
    assert analysis.count_words(text) == 3


def test_count_words_empty():
    assert analysis.count_words("") == 0
