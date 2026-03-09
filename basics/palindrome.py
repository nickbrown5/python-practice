import re

# function to check if string is a palindrome
def is_palindrome(str):
    # chars_to_remove = [' ', ',', '.', '!', '?', ':', ';', '-', '_', '(', ')', '[', ']', '{', '}', '"', "'"]
    # cleaned_str = str
    # for char in chars_to_remove:
    #     cleaned_str = cleaned_str.replace(char, '')
    # cleaned_str = cleaned_str.lower()
    # return cleaned_str == cleaned_str[::-1]
    cleaned_str = ''.join(re.findall(r'[a-z]+', str.lower()))
    return cleaned_str == cleaned_str[::-1]
