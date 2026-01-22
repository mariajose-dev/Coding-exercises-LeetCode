"""
Print the pattern:-
if rows=3
    A 
  A B C 
A B C D E
"""
for i in range(1,n+1):
    ascii_val=65
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("%c"%ascii_val,end=" ")
        ascii_val+=1
        
    print()
