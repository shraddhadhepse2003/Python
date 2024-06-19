#recursion=when a function call itself,then that function is called as recursive function and the process is called as recursion

##def demo():
##    print('shraddha')
##    demo()
##demo()

i=0
def demo():
    global i
    i=i+1
    print('shraddha',i)
    demo()
demo()

import sys
print(sys.getrecursionlimit())
##sys.setrecursionlimit(200)
##print(sys.getrecursionlimit())
##
##i=0
##def demo():
##    global i
##    i=i+1
##    print('shraddha',i)
##    demo()
##demo()
##
###advantage
##1)clean code/less number of code
##2)complex problem can be solved
