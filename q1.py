"""
Zillow Hiring Test Question 1: Given a string convert that to an integer. If the string cannot be converted - throw an exception!

Input: String s
Output: Integer i or an exception

Exceptions: 
    1. The string should be an integer - no decimals, no other characters, not even space
        + and - are valid though
    2. Output integer should be long
"""

import re

class notInteger(Exception):
    """Creating a custom exception"""
    pass

def parse_long(s):
    """Function to parse string"""
    
    neg = 1
    if s[0] == '-':
        s = s[1:]
        neg = -1
    elif s[0] == '+':
        s = s[1:]

    #Checking for non-numeric characters.
    pattern = re.compile(r"[^0-9]")
    if bool(pattern.search(s)) == True:
        """A non-numeric character was found - so return exception!"""
        raise notInteger("Not a number - NaN")
    else:
        integer = 0
        for char in s:
            """Subtracting ASCII value of character from the value 48, which is ASCII value of 0"""
            integer = integer*10 + (ord(char) - 48)

        return neg * integer

print(parse_long('--293213'))