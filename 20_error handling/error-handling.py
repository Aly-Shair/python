# method 1
file = open("test.py", 'w')
try:
    file.write("x = 'hello world'")
finally: 
    file.close()

# method 2(best than above no need to close file or error handlingf it will automaically )
with open("test.txt", "w") as file: 
    file.write("hello world")