def fun_file(dwia):
    def dec_with_arg(*args2):
        print(f"Decorator1 :{dwia}")
        dwia(*args2)
    return dec_with_arg
def class_file(cdwia):
    def StartStopwithargument(*args3):
        print(f"Decorator2 :{cdwia}")
        cdwia(*args3)
    return StartStopwithargument
