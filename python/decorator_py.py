def my_decorator(func):
    def decorator(*args,**kwargs):
        print("decorated start")
        func(*args,**kwargs)
        print("decorated end")
    return decorator

@my_decorator
def my_print(hi="default"):
    print(hi)

my_print("your guy Ganesh Prasad R says hi")