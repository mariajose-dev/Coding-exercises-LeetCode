"""
Given an array of 1's and 0's. 
1. Return a positive number if the count of 1's are more than the count of 0's, 
2. return a negative number if the number of 1's are less than the number of 0's and 
3. return 0 if their counts are same. 
The first input is the number of elements of the binary array followed by the binary array.
"""
a=list(map(int,input().split()))
n=a[0]
one=0
zero=0

for i in range (1,n+1):
    if(a[i]==1):
        one=one+1
    elif(a[i]==0):
        zero=zero+1
    else:
        pass

if(one>zero):
    print(1)
elif(zero>one):
    print(-1)
elif(one==zero):
    print(0)
else:
    pass
