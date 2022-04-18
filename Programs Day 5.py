print("Assignment-1".center(40, "-"))
def noZero(fnc):

    def helper(*args):
        print("Welcome......")
        print(fnc(*args))
    return helper

@noZero
def add(x,y):
    return x+y

@noZero
def sub(x,y):
    return x-y

@noZero
def mul(x,y):
    return x*y

@noZero
def div(x,y):
    return x/y

zero = noZero(mul)
add(10,20)
sub(10,20)
mul(10,20)
div(10,20)

print("Assignment-3".center(40, "-"))

def logBeforeAfter(fnc):
    def helper(*args):
        print("welcome.......")
        fnc(*args)
    return helper


@logBeforeAfter
def fun(x, y):
    print("fun", x, y)

@logBeforeAfter
def fun1(*args):
    print("fun1", args[2])


@logBeforeAfter
def fun2(**kwargs):
    print("fun2", kwargs)

@logBeforeAfter
def fun3(*args, **kwargs):
    print("fun3", args, kwargs)


logBeforeAfter(fun)
fun(10,20)
fun1("A","B","C")
fun2()
fun3(10,11)