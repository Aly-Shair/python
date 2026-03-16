# userscore = input("Enter a value: \n")
# print(type(userscore)) # gives string type value
# print(type(int(userscore))) # gives int type value


age = int(input("Enter your age: "))

# if(age < 13):{
#     print("child")
# }

if age < 13:
    print("child")
elif (age < 20):{
    print("Teenager")
}
elif (age < 60):
    print("Adult")
else:{
    print("Senior")
}