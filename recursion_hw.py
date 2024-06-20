##print your name 10 times without using loop and manually
##a="shraddha "
##print(a*10)


#factorial using recursion
def facto():
    i=1
    fact=1
    num=5
    while i<=num:
        fact=fact*i
        i=i+1
    print(fact)
facto()

##find power of number using recursion
##find prime no. using recursion

##wap to counting no. of digit in given number
a=1234578
b=str(a)
print(str(len(b)))



##fibonacii
##def fibo(n):
##    if n==1:
##        return 0
##    if n==2:
##        return 1
##    return fibo(n-2)+fibo(n-1)
##n=int(input("Enter the number of terms:"))
##print(fibo(n))


##sum of 1st n no. using recursion


##wap for printing n to 1 ......10=10 9 8 7 6 5 4 3 2 1
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    print(i)
    

