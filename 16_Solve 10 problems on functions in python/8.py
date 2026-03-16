# def print_kwargs(name, power):
#     print(name, power)
# print_kwargs(name="alishair", power="infinite")
# print_kwargs(power="infinite", name="alishair")



def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

    for i in kwargs:
        print(i, kwargs[i])
        
print_kwargs(name="alishair", power="infinite")