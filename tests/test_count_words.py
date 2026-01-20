from lib.count_words import *

def test_empty_string():
    assert count_words("") == 0

def test_one_word():
    assert count_words("Hello") == 1

def test_multiple_words():
    assert count_words("Hello my friend how are you? I hope you're well!") == 10

def test_more_punctuation():
    assert count_words("What?! I thought this: you were always, always, always happy") == 10