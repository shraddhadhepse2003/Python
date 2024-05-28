b=[]
a=[1,5,105,15,10,7,8,90]
for i in a:
    for j in range(2,106,1):
        if i%j == 0:
            break
    if i == j:
        b.append(i)
print(b)


c=[]
for i in a:
    i=i+2
    c.append(i)
print(c)


