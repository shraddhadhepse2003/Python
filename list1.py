'''odd=[]
for i in range(1,101,1):
    if i%2 != 0:
        odd.append(i)
print(odd)'''


'''odd=[i for i in range(1,101,2)]
print(odd)'''

    
#print([i for i in range(1,101,2)])

'''a=['robert','anuj','abc']
print([i.upper() for i in a])

print([i for i in a if 'b' in i])'''

'''import random
b=['shraddha','rohit','anushka','yash','shalvi','surbhi']
print(random.choice(b))'''

import random
r=['shraddha','xyz','abc','surbhi','shalvi']
print(random.choice(r))
print(random.choices(r,k=3))
print(random.sample(r,k=2))
random.shuffle(r)
print(r)
print(random.randint(1,10))
print("".join(random.sample('123456789',k=4)))

