# Grammar checker Function Design Recipe


## 1. Describe the Problem

As a user<br>
So that I can improve my grammar<br>
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.


## 2. Design the Function Signature

```python
# EXAMPLE

def grammar_checker(text):
    """Verifies that the input text starts with a capital letter and ends with a suitable punctuation mark.

    Parameters: (list all parameters and their types)
        text - a string

    Returns: (state the return value and its type)
        a boolean that indicates whether the text starts with a capital AND ends with appropriate punctuation

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

```python
# EXAMPLE

"""
Given a correct sentence
Returns True
"""
grammar_checker("Hello world!") => True

"""
Given a lowercase first letter and missing puncuation
Returns False
"""

grammar_checker("hello world") => False

"""
Given a lowercase first letter and correct puncuation
Returns False
"""

grammar_checker("hello world!") => False

"""
Given correct first letter and missing punctuation
Returns False
"""
grammar_checker("Hello world") => False

"""
Given correct first letter and incorrect punctuation
Return false
"""
grammar_checker("Hello world:") => False

"""
Given an empty string
Throws error
"""
grammar_checker("") => "Please enter a sentence"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
