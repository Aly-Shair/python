# No, if statements, for loops, and while loops do not create a new scope in Python. Unlike functions, which create a new local scope, loops and conditionals operate within the same scope where they are defined.

# user = "alishair"
# def func():
#     # user = "lionheart"
#     print(user)
# func()
# print(user)

# x = 10
# for i in range(2):
#     x  = 19
#     print(x)
# print(x)

# x = 99
# def func():
#     # x = 88 # error SyntaxError: name 'x' is assigned to before global declaration
#     global x
#     x = 88 # no error after global x
#     print(x)
# func()
# print(x)
# print(x)
# func()


# x = 99
# def func1():
#     x = 88
#     def func2():
#         print(x)
#     # func2()
#     # return func2() # it will execute and not send ref but send its value
#     return func2 # it will send ref

# x = func1()
# print(x)
# x() # it will exe func2 # sirf function ka address  nahi jana us function kay andar vars han unka ref bhi jana ha isko boltay han bag theory and it is a closure concept

def chaicoder(num):
    def actual(x):
        return  x**num
    return actual
# python ma inko factory function ka nam se bhi jana jata ha or closure ka name se bhi
result = chaicoder(2)
actual_result = result(3)
print(actual_result)