def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()

        print("After function call")
    return wrapper

@simple_decorator
def greet():
    print("Hello!")

print(greet())

