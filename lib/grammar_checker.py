def grammar_checker(text):
    allowed_punctuation = ".?!"
    if len(text) == 0:
        raise Exception("Please enter a sentence.")
    return text[0].isupper() and text[-1] in allowed_punctuation
        

'''
allowed_punctuation was originally a list
but this can be done as a string too which is slightly easier
'''