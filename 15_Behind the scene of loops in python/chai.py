myList = [1, 2, 3, 4]
# I = iter(myList)
# print(I)
# print(I.__next__())
# print(I.__next__())
# print(I)
# print(I.__next__())
# print(I.__next__())
# print(I.__next__()) # error

# f = open("main.py")
# iter(f) # no need to I = iter(f) cuz python internally do it for files
# print(iter(f) is f)
# print(iter(f) is f.__iter__())
# print(iter(f) is f.__next__())

d = {
    'a': 1,
    'b': 2
}
# for key in d:
# # for key in d.keys():
#     print(key)
# I = iter(d)
#  # both are same
# print(I.__next__())
# print(next(I))
# print(I.__next__())

# r = range(5)
# I = iter(r)
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I))
# # print(next(I)) # Err: StopIteration