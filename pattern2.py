"""
Print the Pattern
rows=3
A 
A B 
A B C 
"""
n=int(input())
for i in range (1,n+1):
    ascii_val=65
    for j in range (1,i+1):
        print("%c"%ascii_val,end=" ")
        ascii_val+=1
    print()
    
