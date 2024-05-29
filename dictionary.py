a={'name':'ABC',0:'kuch bhi','age':21}
print(a)
print(len(a))
print(type(a))

a['age']=20

a['city']='thane'
#a['name']='Shraddha'
print(a)


for i in a:
    print(f"{i} = {a[i]}")


for i in a:
    print(f"{i}")

keys=['name','age','city']
values=['xyz',33,'thane']
data={}
for i in range(len(keys)):
    data[keys[i]]=values[i]
print(data)

