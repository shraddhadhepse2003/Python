a=['robErt','anUj','mishraji','saud','jadhav','nair']
'''i=0
while i<len(a):
    j=0
    c=0
    while j<len(a[i]):
        if a[i][j] in 'aeiou':
            c=c+1
        j+=1
    print(f"{a[i]} this name contains {c} vowels")
    i+=1

i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if len(a[i])==4:
            print(a[i])
            break
        j+=1
        
    
    i+=1


for i in a:
    for j in a:
        if len(i)==4:
            print(i)
            break

for i in a:
    c=0
    for j in a:
        if j in 'aeiou':
            c=c+1
            print(i)
            break

        
for  i in a:
    if len(i)==6:
        print(i)'''




for i in a:
    c=""
    for j in i.lower():
        if j in 'aeiou':
            c=c+j
    print(f"{i} this name contains {len(c)} ({c}) vowels")
            






