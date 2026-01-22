import datetime
import math

def age_checker(dob):
    if dob == '':
        return "Please enter your DOB in the format 'YYYY-MM-DD'."
    
    if not dob[0:4].isnumeric() or not dob[5:7].isnumeric() or not dob[8:10].isnumeric():
        return "Please enter your DOB in the format 'YYYY-MM-DD'."

    year = int(dob[0:4])
    month = int(dob[5:7])
    day = int(dob[8:10])

    birthday = datetime.datetime(year, month, day)
    today = datetime.datetime.now()
    age = today - birthday 
    if age.days / 365 > 16: 
        return 'Access granted' 
    else: 
        return f"Access denied, you are {math.floor(age.days / 365)}. You must be 16."
    
