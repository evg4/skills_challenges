# Age checker Function Design Recipe


## 1. Describe the Problem

As an admin<br>
So that I can determine whether a user is old enough<br>
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin<br>
So that under-age users can be denied entry<br>
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin<br>
So that old enough users can be granted access<br>
I want to send a message to any user aged 16 or older to say that access has been granted.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def age_checker(dob):
    """Send a message to user depending on age

    Parameters: (list all parameters and their types)
        dob - a string in format 'YYYY-MM-DD' 

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])
        a string - sentence with outcome

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
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
age_checker('1995-04-01') > "Access granted."
age_checker('2020-04-01') > "Access denied. You are 5. You must be 16.
age_checker('2010-01-22') > "Access granted."
age_checker('2010-01-23') > "Access denied. You are 15. You must be 16.
age_checker('') > "Please enter your DOB in the format 'YYYY-MM-DD'."
age_checker('23-01-1990') > "Please enter your DOB in the format 'YYYY-MM-DD'."
age_checker(1990-01-23) > "Please enter your DOB in the format 'YYYY-MM-DD'."



## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE



"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""

```

Ensure all test function names are unique, otherwise pytest will ignore them!
