row=1
while row<=5:
    col=1
    while col<=5:
        if col<=row:
            print(row,end=" ")
        col+=1
    row+=1
    print()
