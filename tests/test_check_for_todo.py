from lib.check_for_todo import *

def test_sentence_with_TODO_at_end_returns_true():
    assert check_for_todo("Make cup of tea #TODO") == True

def test_sentence_with_TODO_at_beginning_returns_true():
    assert check_for_todo("#TODO Make cup of tea") == True

def test_sentence_with_TODO_in_middle_returns_true():
    assert check_for_todo("Make #TODO cup of tea") == True

def test_sentence_without_TODO_returns_false():
    assert check_for_todo("Make cup of tea") == False

def test_sentence_with_no_hashtag_returns_false():
    assert check_for_todo("TODO Make cup of tea") == False

def test_empty_string():
    assert check_for_todo("") == False