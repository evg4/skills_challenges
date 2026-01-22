from lib.age_checker import *

def test_grants_access_when_over_16():
    assert age_checker('1995-04-01') == 'Access granted'

def test_denies_access_when_under_16(): 
    assert age_checker('2020-04-01') == 'Access denied, you are 5. You must be 16.'

def test_empty_string_entered(): 
    assert age_checker('') == "Please enter your DOB in the format 'YYYY-MM-DD'."

def test_wrong_format_date(): 
    assert age_checker('23-01-1990') == "Please enter your DOB in the format 'YYYY-MM-DD'."

def test_incorrect_month_name(): 
    assert age_checker('1990-april-07') == "Please enter your DOB in the format 'YYYY-MM-DD'."

# def age_checker('23-01-1990') > "Please enter your DOB in the format 'YYYY-MM-DD'."
# def age_checker(1990-01-23) > "Please enter your DOB in the format 'YYYY-MM-DD'."