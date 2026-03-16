def even_generator(limit):
    li = []
    for i in range(0, limit+1, 2):
        # print(i)
        li.append(i)
    return li
print(even_generator(10))

# def even_generator(limit):
#     for i in range(0, limit+1, 2):
#         # return i
#         yield i #  value ye bhi return karta ha but memory me usko rakhta ha or sirf function ko nah rakhta uski state ko bhi rakhta ha kay abhi ap itna kam kar chukay ho

# print(even_generator(10))

# for i in even_generator(10): # error if not returning list
#     print(i)