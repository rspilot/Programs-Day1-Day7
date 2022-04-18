def fun_file(dec):
    def begin_end(*args):
        print(f"Decorator1 :{dec}")
        dec(*args)
    return begin_end
def class_file(dwa):
    def StartStop(*args1):
        print(f"Decorator2 :{dwa}")
        dwa(*args1)
    return StartStop



