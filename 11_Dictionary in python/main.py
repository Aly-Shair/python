chai_types = {
    "Masala": "Spicy",
    "Ginger": "Zesty",
    "Green": "Mild"
}
print(chai_types)

# print(chai_types["Masala"])
# print(chai_types["Ginger"])
# print(chai_types.get("Green"))

# for key not exist
# print(chai_types.get("Greeny")) # it gives none
# print(chai_types["Ginger"]) # it gives error

# Updating the dict
# print(chai_types)
# chai_types["Ginger"] = "Mint" # correct
# chai_types.get("Green")  = "Mint" # wrong 
# print(chai_types)

# for chai in chai_types:
#     print(chai, chai_types[chai])

# for key, value in chai_types.items(): # "chai_types.items()" refers to each item(key+value) in the dict
#     print(key, value)
     
# if "Masala" in chai_types:
#     print("Masala is present")
# else: 
#     print("Masala is absent")

# print(len(chai_types))


# chai_types["Earl Grey"] = "Citrus"
# print(chai_types)
# print(chai_types.pop("Ginger"))
# print(chai_types)
# print(chai_types.popitem()) # pops from last of dict
# print(chai_types)
# del chai_types["Green"] # deletes from memory
# print(chai_types)

# chai_types_copy = chai_types.copy();
# print(chai_types_copy)

# tea_shop = {
#     "chai":{
#         "Masala": "Spicy",
#         "Ginger": "Zesty",
#     },
#     "tea":{
#         "Green": "Mild",
#         "Black": "Strong"
#     }
# }
# print(tea_shop)
# print(tea_shop["chai"])
# print(tea_shop["chai"]["Ginger"])
# print(tea_shop.get("chai").get("Ginger"))
# for key, value in tea_shop.items():
#     print(key, value)

# squared_nums = {x:x**2 for x in range(11)}
# print(squared_nums)

# print(squared_nums.clear()) # clear all obj
# print(squared_nums)

# keys = ["Masala", "Ginger", "Mint"]
# default_value = "delecious"
# new_dict = dict.fromkeys(keys, default_value)
# print(new_dict)
# new_dict = dict.fromkeys(keys, keys)
# print(new_dict)