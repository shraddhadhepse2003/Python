a={'name':'abc','age':60,'city':'thane'}
print(a['name'])
print(a.get('name'))
print(a.get('age'))

a['phone']=9568940040
a.update({'tel':9594040399})
a.pop('name')
a.popitem()
#a.clear()
del a['age']
print(a)
