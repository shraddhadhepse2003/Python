'''row=97
i=1
while row<=101:
    cols=1
    while cols<=5-i:
        print(" ",end=" ")
        cols+=1
    col=97
    while col<=row:
        print(chr(row),end=" ")
        col+=1
    i+=1
    row+=1
    print()'''

row=97
while row<=101:
    col=101
    while col>=97:
        if col<=row:
            print(chr(row),end=" ")
        else:
            print(" ",end=" ")
        col -= 1
    row += 1
    print()
