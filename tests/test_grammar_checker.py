from lib.grammar_checker import *
import pytest

def test_uppercase_and_exclamation_mark():
    assert grammar_checker("Hello World!") == True

def test_uppercase_and_fullstop():
    assert grammar_checker("Hello World.") == True

def test_lowercase_and_missing_punctuation():
    assert grammar_checker("hello world") == False

def test_lowercase_and_correct_punctuation():
    assert grammar_checker("hello world!") == False

def test_uppercase_and_missing_punctuation():
    assert grammar_checker("Hello world") == False

def test_uppercase_and_incorrect_punctuation():
    assert grammar_checker("Hello world:") == False

def test_empty_string():
    with pytest.raises(Exception) as e:
        grammar_checker("")
    error_message = str(e.value)
    assert error_message == "Please enter a sentence."