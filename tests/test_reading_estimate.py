from lib.reading_estimate import *

def test_200_words():
    twenty_string = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteens eventeen eighteen nineteen twenty "
    long_string = ""
    for i in range(0,10):
        long_string = long_string + twenty_string
    assert reading_estimate(long_string) == "60 seconds"

def test_20_words():
    twenty_string = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteens eventeen eighteen nineteen twenty"
    assert reading_estimate(twenty_string) == "6 seconds"

def test_empty_string():
    assert reading_estimate("") == "0 seconds"