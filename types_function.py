##types of argument
##1)Positional argument
##2)default argument
##3)keyword argument
##4)variable length argument


1)Positional argument
during a function call,values passed through arguments should be in the order of parameters in the function definition

##def simple_int():
##    print('principle is',p)
##    print('rate is',r)
##    print('time is',t)
##    si=p*r*t/100
##    print('simple intrest is:',si)
##p=5000
##r=10
##t=5
##simple_int()

`
##def simple_int(r,p,t):
##    print('principle is',p)
##    print('rate is',r)
##    print('time is',t)
##    si=p*r*t/100
##    print('simple intrest is:',si)
##p=5000
##r=10
##t=5
##simple_int(p,r,t)

def simple_int(x,y,z):
##    print('principle is',p)
##    print('rate is',r)
##    print('time is',t)
    print('principle is',p)
    print('rate is',r)
    print('time is',t)
    si=p*r*t/100
    print('simple intrest is:',si)
p=5000
r=10
t=5
simple_int()

