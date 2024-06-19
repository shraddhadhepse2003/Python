#append
a=[1,2,3,'abc','xyz']
a.append("added")
print(a)

#extend
a=[1,2]
b=[3,4]
a.extend(b)
b.extend(a)
print(a)
print(b)

#insert
a=[1,2,3,4]
a.insert(0,100)
a.insert(0,100)
a.insert(2,300)
a.insert(2,400)
print(a)

#using index
a=['abc',100,200]
a[1]='shraddha'
print(a)


#pop
a=[1,2,3,4]
a.pop()
#a.remove('abc')
print(a)

#del
a=[1,2,3,4,4]
del a[0]
print(a)

ab=[1,2,3,3,3]
print(ab.count(3))

#clear
a=[1,2,3,5,7,8]
a.clear()

print(ab.index(3))
ab.reverse()
print(ab)
