"""
Write a program to read a sentence and return the number of words present in the sentence.
"""

string = list(map(str,input().split()))
# print(string)
co = 0

for item in string:
    co = co + 1

print(co)
