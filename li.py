'''a=[[['robert','mishraji','anuj','rajith','jadhav']]]
for i in a[0][0]:
    print(i)



a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in a:
    for j in i:
        print(j)'''


a=[[['robert','mishraji','anuj','rajith','jadhav']]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        k=0
        while k<len(a[i][j]):
            print(a[i][j][k])
            k+=1
        j+=1
    i+=1


a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1
