items = ["apple", "banana", "orange", "apple", "mango"]

# for item in items:
#     if (items.count(item) > 1):
#         print("not unique", item)
#         exit()        
# print("unique")

unique_items = set()

for item in items:
    if item in unique_items:
        print("dublicate: ", item)
        exit()
    else:
        unique_items.add(item)

print("unique")
