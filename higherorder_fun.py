#higher order function
##A function which takes another as an argument is called as higher order function
##
##Built in higher order function
##1)filter function
##2)map function
##3)reduce function




##number=[11,22,33,44,55,66]
##def even_fun(x):
##    if x%2==0:
##        return True
##filter_object=filter(even_fun,number)
##print(filter_object)

##number=[11,22,33,44,55,66]
##def even_fun(x):
##    if x%2==0:
##        return True
##filter_object=filter(even_fun,number)
##print(list(filter_object))

##number=[11,22,33,44,55,66]
##def even_fun(x):
##    if x%2==0:
##        return True
##filter_object=list(filter(even_fun,number))
##print(filter_object)
##print(filter_object)


number=[45,77,88,33,48,50,13]
def prime_fun(x):
    for i in range(2,101,1):
        if x%i == 0:
            break;
    if x==i:
            return True
        
filter_object=list(filter(prime_fun,number))
print(filter_object)



#map function
#this is also built in higher order function,it apply specific function on each element of the iterable and perhaps change element

##n=[1,2,3,4,5,6]
##def square(x):
##    return x*x
##y=list(map(square,n))
##print(y)

##n=[1,2,3,4,5,6]
##def facto(x):
##    i=1
##    fact=1
##    while i<=x:
##        fact=fact*i
##        i=i+1
##    return fact
##a=list(map(facto,n))
##print(a)
