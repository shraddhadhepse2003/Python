a=[1,2,3,4,5,6,7,7,6]
c=0
for i in range(0,len(a),1):
    c1=0
    for j in range(i+1,len(a),1):
        if a[i] == a[j]:
            c1=c1+1
            c=c+1
            print(f"duplicates numbers are {a[i]}={c1}")
print(f"total duplicates {c}")
            
