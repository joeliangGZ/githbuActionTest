import pytest
from app.string_utils import (
    reverse_string,
    capitalize_words,
    remove_whitespace,
    count_words,
    is_palindrome,
)


class TestReverseString:
    def test_reverse_basic(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty(self):
        assert reverse_string("") == ""

    def test_reverse_single_char(self):
        assert reverse_string("a") == "a"

    def test_reverse_palindrome(self):
        assert reverse_string("madam") == "madam"


class TestCapitalizeWords:
    def test_capitalize_basic(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_capitalize_already(self):
        assert capitalize_words("Hello World") == "Hello World"

    def test_capitalize_empty(self):
        assert capitalize_words("") == ""


class TestRemoveWhitespace:
    def test_remove_spaces(self):
        assert remove_whitespace("hello world") == "helloworld"

    def test_remove_multiple_spaces(self):
        assert remove_whitespace("hello   world") == "helloworld"

    def test_remove_tabs(self):
        assert remove_whitespace("hello\tworld") == "helloworld"


class TestCountWords:
    def test_count_basic(self):
        assert count_words("hello world") == 2

    def test_count_single_word(self):
        assert count_words("hello") == 1

    def test_count_empty(self):
        assert count_words("") == 0

    def test_count_multiple_spaces(self):
        assert count_words("hello   world") == 2


class TestIsPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome("madam") is True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("madam madam") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_empty_string(self):
        assert is_palindrome("") is True
