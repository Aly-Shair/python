# chai = "Lemon Tea"
# print(chai)
# chai = """Triple Tea"""
# print(chai)
# chai = "'Masala Tea'"
# print(chai)

# print("""Hello 
#       World""")
# chai = 'Masala Chai'
# slice_chai = chai[0:6]
# print(slice_chai)
# slice2 = chai[-1: 4]
# slice2 = chai[-1: -4]
# print(slice2)

num_list = "0123456789"
# print(num_list[:])
# print(num_list[3:])
# print(num_list[:7])
# print(num_list[0:6:2])
# print(num_list[-4: 9])
# print(num_list[-4:])
# print(num_list[0:6:1])
# print(num_list[0:6:3])

# chai = "Masala Chai"
# print(chai.lower())
# print(chai.upper())

# chai = "    Masala Chai    "
# print(chai)
# print(chai.strip()) # remove spaces from left and right
# print(chai)

# chai = "Lemon Chai"
# print(chai.replace("Lemon", "Ginger"))
# print(chai.replace("xyz", "Ginger"))
# print("0123456789".replace("", "Ginger"))
# print(chai.replace(" ", "Ginger"))
# print(chai)

# chai = "Lemon, Ginger, Mint, Masala"
# print(chai.split())
# print(chai.split(","))
# print(chai.split(", ")) # string convet to list using split

# chai = "Lemon Chai Chai"
# print(chai.find("Chai"))
# print(chai.find("Tea"))
# print(chai.count("Chai"))
# print(chai.count("Tea"))

# chai_type = "Masala"
# quantity = 2
# # print(f"I ordered {quantity} cups of {chai_type} chai") # {} are placeholders to add variables
# order = "I ordered {} cups of {} chai"
# print(order.format(quantity, chai_type))


# chai_variety = ["Lemon", "Masala", "Ginger", "Mint"]
# print("".join(chai_variety))
# print(" ".join(chai_variety))
# print("-".join(chai_variety))
# print(" 1 ".join(chai_variety))
# print(len(chai_variety))

# chai = "Masala Chai"
# print(len(chai))

# for letter in chai:
#     print(letter)


# chai = "He said, \"Masala chai is awesom\""
# print(chai)

# chai =r"Masala\nChai"
# print(chai)

# chai ="Masala\nChai"
# print(r""+chai)

# chai =r"c:\user\administrato"
# chai =r"c:\user\administrato\" 
# error due to last slash use \\ for no error
# print(chai)

# chai ="c:\\user\\administraton\\" # slashed are unicode chars so to handle them use one more backlash
# print(chai)
# print(chai.split("\\"))

chai = "Masala Chai"
print("Masala" in chai)
print("a " in chai)
print("masala" in chai)
print("sala" in chai)
print("" in chai)
print(" " in chai)