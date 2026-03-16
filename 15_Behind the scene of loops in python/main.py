import time
""
''
print("hello main 1")
print("hello main 2")

# >>> f = open("main.py")
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'print("hello main 1")\n'
# >>> f.readline()
# 'print("hello main 2")'
# >>> f.readline()
# ''
# >>> f.readline()
# ''
# >>> 


# >>> f = open("main.py")
# >>> f.__next__()
# 'import time\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# 'print("hello main 1")\n'
# >>> f.__next__()
# 'print("hello main 2")\n'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<python-input-26>", line 1, in <module>
#     f.__next__()
#     ~~~~~~~~~~^^
# StopIteration
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<python-input-27>", line 1, in <module>
#     f.__next__()
#     ~~~~~~~~~~^^
# StopIteration
# >>> 
# >>> 


# >>> for line in open("main.py").readlines()
# >>> for line in open("main.py"):
# ...     print(line)
# ...  


# >>> while True:
# ...     line = f.readline()
# ...     if not line: break
# ...     print(line, end="")