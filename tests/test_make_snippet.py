from lib.make_snippet import *

def test_make_snippet_short_input():
    assert make_snippet("Today I ate a cake.") == "Today I ate a cake."

def test_make_snippet_long_input():
    assert make_snippet("Today I ate a chocolate cake and it was great!") == "Today I ate a chocolate..."

def test_make_snippet_one_word_input():
    assert make_snippet("Hello!") == "Hello!"

def test_make_snippet_empty_string():
    assert make_snippet("") == ""

def test_make_snippet_include_commas():
    assert make_snippet("Wow, are you, Brian, really my friend?") == "Wow, are you, Brian, really..."