def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join([f"{k} = {v}" for k, v in kwargs.items()])
        # kwargs_value = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"function: {func.__name__} calling with args: {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper


@debug
def hello():
    pass

@debug
def greet(name, hello, greeting="Hello"):
    # pass
    print(f"{greeting}!, {name}")

greet("alishair",hello = "world", greeting="kasey ho")
# hello()