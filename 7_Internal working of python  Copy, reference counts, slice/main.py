# >>> import sys
# >>> sys.getrefcount(14601)
# 3   
# >>> sys.getrefcount(1)
# 4294967295
# >>> sys.getrefcount("alishair")
# 3   
# >>> sys.getrefcount("hello")
# 3   
# >>> sys.getrefcount("1")
# 4294967295

# myListOne = [1, 2, 3];
# myListTwo = myListOne;
# myListOne = "alishair";
# print(myListTwo);
# # myListOne = [1, 2, 3];
# myListOne = myListTwo;
# myListOne[0] = 33;
# print(myListOne);
# print(myListTwo);

# h1 = [1, 2, 3]
# h2 = h1[:] # it will create a copy cuz we are slicing and create a new ref
# h1[0] = 43
# print(h1)
# print(h2)

# import copy
# h1 = [1, 2, 3]
# h2 = copy.copy(h1) # creating copy
# h2 = copy.deepcopycopy(h1) #  deepcopy means list ak andar bhi koi list ha to lay ao

m = [1, 2, 3]
# n = m
n = [1, 2, 3]
print(m == n)
print(m is n) # is checks memory refs