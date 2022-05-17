# Print function
M = "Machine"
L = "Learning"

print("Test")
print(M + L)

# Math operations
print(1+3)

# Data types
print(type(M))
print(type(7.5))

# Constant and variable
hero1,hero2,hero3 = "ironman","hulk","thor"

print(hero1)
print(hero2)
print(hero3)

# Input function

name = input("Type your name:")
if name == "":
    name = input("Please input the right name:")
else:
    pass

age = int(input("Enter your age:"))
if age<=0:
    age = int(input("Please enter the right age:"))
else:
    pass

Civil_status = bool(input("Are you from Indonesia? (Type 1 if yes; type 0 if no)"))
if Civil_status == True:
    Civil_status = "Indonesia"
else:
    Civil_status = "Not Indonesia"

print("The summary:\n")
print("Name:", name)
print("Age:", age)
print("Civil status:", Civil_status)
print("\n")



