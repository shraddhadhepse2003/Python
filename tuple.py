'''a=(1,2,3,'abc','xyz')
print(a)
print(type(a))
print(len(a))
print(a[-1])


b=(1,2)
print(a+b)
s=(1,)
print(type(s))

data=('shraddha',21,'thane',11,222,33,44,55,66,77)
(name,age,city,*a)=data
print(city)
print(a)
print(a[3])'''


'''a=[1,2,3,([33,88,'abc',('yes','no','yes')])]
#a[3][3]=('yes','yes','yes')
b=list(a[3][3])
b[1]='yes'
#print(tuple(b))
a[3][3]=tuple(b)
print(a)'''

a=(1,2,3,4,4)
print(a[::-1])
print(a.count(4))
print(a.index(1))

#tuple inside list is replacable
for i in a:
    print(i)

i=0
while(i<len(a)):
    print(a[i])
    i+=1

for i in range(len(a)):
    print(a[i])
    
