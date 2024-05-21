n=8208 #153  
n1=n
l=len(str(n))
s=0
while n!=0:
    r=n%10
    s=s+r**l
    n=n//10
if n1 == s:
    print("The number is armstrong")
else:
    print("The number is not armstrong")
