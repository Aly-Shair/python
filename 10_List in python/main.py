tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)
# print(tea_varities[0])
# print(tea_varities[1])
# print(tea_varities[2])
# print(tea_varities[-1])
# print(tea_varities[-2])
# print(tea_varities[-3])
# print(tea_varities[: 2])
# print(tea_varities[2:])
# print(tea_varities[-1:])
# print(tea_varities[1:3])

# tea_varities[3] = "Herbal"
# print(tea_varities)
# tea_varities[2:3] = "Lemon"
# print(tea_varities)
# tea_varities[2:3] = ["Lemon"]
# print(tea_varities)
# tea_varities[1:3] = ["Lemon"]
# print(tea_varities)
# tea_varities[:] = "Lemon"
# print(tea_varities)

# print(tea_varities[1:3])
# tea_varities[1:3] = ["Blue", "Green"]
# print(tea_varities)

# print(tea_varities[1:1])
# tea_varities[1:1] = ["test", "test"]
# print(tea_varities)
# tea_varities[1:3] = []
# print(tea_varities)

# for tea in tea_varities:
#     print(tea)

# for tea in tea_varities:
#     print(tea, end=" - ")

# if "Oolong" in tea_varities:
#     print("i have tea")
# else: 
#     print("i don t have")

# tea_varities.append("Herbal") # append adds in the last of list
# print(tea_varities)
# print(tea_varities.append("Herbal"))
# print(tea_varities)


# tea_varities.pop();
# print(tea_varities)
# print(tea_varities.pop())
# print(tea_varities)

# tea_varities.remove("Green")
# print(tea_varities)
# tea_varities.remove("Herbal") # remove not return anything
# print(tea_varities)
# tea_varities.remove("Herbal")
# print(tea_varities)
# tea_varities.remove("Green")
# print(tea_varities)
# tea_varities.remove("Why") # ValueError: list.remove(x): x not in list
# print(tea_varities)

# print(tea_varities.remove("Black"))

# tea_varities.insert(1, "level") # dont return anything
# print(tea_varities)

# tea_varities_copy = tea_varities.copy()
# print(tea_varities_copy)
# tea_varities_copy.append("Herbal")
# print(tea_varities_copy)
# print(tea_varities)

# [] square brakets are list comprehension
# squared_nums = [] 

# >>> range
# <class 'range'>
# >>> range(10)
# range(0, 10)
# >>> range(1, 10)
# range(1, 10)
# >>> y = range(10)
# >>> y
# range(0, 10)
# >>> y = range(1, 10)
# >>> y
# range(1, 10)
# >>> print(y)
# range(1, 10)

squared_nums = [x**2 for x in range(10)] # python range in exclusive so 10 not include
print(squared_nums)
squared_nums = [x for x in range(10)] # it is called list comprehesion
print(squared_nums)