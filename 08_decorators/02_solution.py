
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f'{key}={value}' for key, value in kwargs.items())
        print(f'{func.__name__}({args_value}, {kwargs_value})')
        return func(*args, **kwargs)
    
    return wrapper

@debug
def hello():
    print("Hello!")

@debug
def greet(name, greeting='Hello'):
    return f'{greeting}, {name}!'
hello()
print(greet('John'))