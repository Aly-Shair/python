# list is mutable
# tuple is immutable

tea_types = ("Masala", "Green", "Oolong")
print(tea_types)

# print(tea_types[0])
# print(tea_types[1])
# print(tea_types[2])

# print(tea_types[-1])
# print(tea_types[-2])
# print(tea_types[-3])

# print(tea_types[:])
# print(tea_types[1:])
# print(tea_types[:1])


# tea_types[0] = "Lemon" # error cuz tuple is immutable

# print(len(tea_types))

# tea_types_copy = tea_types
# print(tea_types_copy)

more_tea = ("Lemon", "Mint")
all_tea = tea_types+more_tea
# print(all_tea)

# if "Green" in all_tea:
#     print("present")

# more_tea = ("Herbal", "Earl Grey", "Herbal")
# print(more_tea)
# print(more_tea.count("Herbal"))

# to unpack tuple left len = right len
# (Masala, green, oolong) = tea_types
# (Masala, green, oolong, lvl) = tea_types # error to many values to unpack and no enough value to unpack
# print(Masala)
# print(green, oolong)

# tea_types = ("Masala", "Green", "Oolong", "Mint")
# (Masala, green, oolong) = tea_types # error

print(type(tea_types))

# nested tuple

nested = ("hello", ("Hello", "World"), "world", "", {"ali": "shair"}, ['ali', 2])
print(nested)
