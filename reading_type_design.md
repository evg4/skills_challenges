# Reading time Function Design Recipe

## 1. Describe the Problem

As a user<br>
So that I can manage my time<br>
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_reading_time(text):
    """Estimates reading time, assuming a speed of 200 words per minute

    Parameters: (list all parameters and their types)
        text -  string

    Returns: (state the return value and its type)
        returns an easy-to-read string stating length of time and units, e.g. "5 minutes 27 seconds", "2 days 3 hours 5 minutes".
        NOTE: assume it will be best to calculate in ms then convert before returning, but check options

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string with 200 words
It will return "60 seconds"
"""
estimate_reading_time()

"""
Given a string with 20 words
It will return "6 seconds"
"""
estimate_reading_time("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteens eventeen eighteen nineteen twenty") >> "6 seconds"

"""
Given an empty string
It will return "0 seconds"
"""
estimate_reading_time("") >> "0 seconds"

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._



Ensure all test function names are unique, otherwise pytest will ignore them!
