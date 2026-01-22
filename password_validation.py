"""
Write a program to check if the given password is strong. Return 1 if the password is strong and 0 if the password is weak.

A strong password is one which satisfies the following conditions:

It contains a mix of capital letters, small letters and digits.
It contains minimum 8 characters.
It contains atleast one non alphanumeric character.
It should not contain any space.
Example:

Input:

myname123

Output:

0

Input:

Myname123$

Output:

1
"""
def function(text):
    hasDigit = 0
    hasUpper = 0
    hasLower = 0
    hasSpecial = 0
    count=0

    for s in text:
        if s == ' ':
            return 0
        if 'A' <= s <= 'Z':
            hasUpper = 1
        elif 'a' <= s <= 'z':
            hasLower = 1
        elif '0' <= s <= '9':
            hasDigit = 1
        else:
            hasSpecial = 1   # any non-alphanumeric
        count=count+1

    if hasUpper and hasLower and hasDigit and hasSpecial and count>8:
        return 1
    else:
        return 0


text = input()
print(function(text))
