def check_age(age):
    '''
        This checks that the user has entered valid data.
        Age cannot be less than 12, or older than 114.
    '''
    if isinstance(age, str) or isinstance(age, float):
        return "Please enter an integer (i.e. a number which doesn't have a decimal)."
    elif age < 12:
        return "Please enter an integer that is more than (or equal to) 12."
    elif age > 114:
        return "Please enter an integer that is less than 115."

    return "Thank you"

