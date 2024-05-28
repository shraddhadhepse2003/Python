a=['robert','anuj','mishraji','saud','jadhav','nair']
b=[]
for i in a:
    for j in i:
        if j == 'r':
            b.append(i)
            break
print(b)
