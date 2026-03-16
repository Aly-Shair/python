def sum_all(*args):  # you can use array but in python it is easy # * is necessary
    # pass

    # print(args) # gives a tuple
    # print(*args)
    # return sum(args)

    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(2, 2, 2))