#wap for fibbonacci series using recursion
##0,1,1,2,3,5,8,13,21,34
##fibbo(1)=0
##fibbo(2)=1
##fibbo(3)=fibbo(1)+fibbo(2)
##fibbo(3)=fibbo(3-2)+fibbo(3-1)
##fibbo(n)=fibbo(n-2)+fibbo(n-1)

def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-2)+fibo(n-1)
n=int(input("Enter the number of terms:"))
print(fibo(n))






##print your name 10 times without using loop and manually
##factorial using recursion
##find power of number using recursion
##find prime no. using recursion
##wap to counting no. of digit in given number
##fibonacii
##sum of 1st n no. using recursion
##wap for printing n to 1 ......10=10 9 8 7 6 5 4 3 2 1
