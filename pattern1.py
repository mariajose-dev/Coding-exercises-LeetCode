"""
Print the Pattern
for rows=4
      A 
    B A B 
  C B A B C 
D C B A B C D 
"""
n = int(input("Enter the value on n/rows:"))        # number of rows

for i in range(1, n + 1):   # row loop

    for s in range(1, n - i + 1):  # print leading spaces
        print(" ", end=" ")

    ascii_val = 64 + i     # starting alphabet for each row

    for j in range(1, 2 * i):  # print alphabets in pyramid form
        print("%c" % ascii_val, end=" ")

        if j < i:          # move left side (decreasing letters)
            ascii_val -= 1
        else:              # move right side (increasing letters)
            ascii_val += 1

    print()                # move to next line
