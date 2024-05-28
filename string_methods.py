'''a="HELLO EVERYONE"
print(a.lower())
b="hello world"
print(b.upper())
print(b.capitalize())
print(a)


#list
c=list((1,2,'abc','xyz'))
print(c)
print(type(c))
print(len(c))

d=[22,56,44,'abc','fkg']'''

e=['robert','anuj','mishraji','saud','jadhav','nair']
'''for i in e:
    if i[-1]=='i':#if len(a)-1=i
        print(i)'''

'''for i in e:
    if 'r' in i:
        print(i)'''



i=0
while i<len(e):
    j=0
    while j<len(e[i]):
        if e[i][j]=='r':
            print(e[i])
            break
        j+=1
    i+=1


