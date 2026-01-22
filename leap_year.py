'''
Write a program to check if a given year is leap year or not. 

Return the year if it is a leap year.

Return 0 if it is not a leap year.

Note: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. 
'''

yr=int(input())

if(yr%4==0 and (yr%100!=0 or yr%400==0)):
    print(yr)
else:
    print(0)
