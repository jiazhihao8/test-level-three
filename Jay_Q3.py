# 3) Topic - Testing in Python  (10 marks)
# Create a .py file and name it yourname_Q3.py, now copy paste the following code given below and run a doc test!

def is_anagram(a_word, b_word):
    """
    >>> is_anagram("abc", "acb")
    True
    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("one", "two")
    False
    >>> is_anagram("anagram", "nag a ram")
    True
    """
    return sorted(a_word) == sorted(b_word) 
# After running the doctest tell me what the error is? And why is there an error?
# How to fix the error?
# You can comment on the line having error using #.
# Hint: Search for python sort function if you haven't used this before!