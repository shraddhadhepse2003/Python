'''a
ab
abc
abcd
abcde

    a
   bb
  ccc
 dddd
eeeee'''
col=97
while col<=101:
    row=97
    while row<=col:
        print(chr(row),end=" ")
        row=row+1
    col=col+1
    print()
        
  
