#Booleans

# a = True
# b = False
#
# print(a == b) #False
# print(a != b) #True
# print(a >= True) #True
# # print(b <= False) #True
#
# print(True and False) #False due to the "and" operator
# print(False and True) #False
# print(False and True) #True

#Booleans are useful for quickly checking the state of something.
#Also useful for validating data types

#Booleans with Data types
#
# hi = "Hello World!"
# print(hi.isalpha()) #False / Checks if every is alpha numeric
# print(hi.islower()) # Because H is upper case
# print(hi.endswith("!"))
# print(hi.startswith("H")) #lower case and upper case sensative
#
# x = 0
# y = 10
# print(bool(x)) # Zero is considered always false
# print(bool(y)) #All number true even minus


#None

#None = Null in other languages

print(bool(None)) # Always False

x = None # Can be used when not wanting to assign a variable to a value

print(x == False) #False
print(x == True) # False

# checking if a variable is None

print(x == None) # direct comparison = More complex
print(x is None) # Best practice for checking if something is None/ None is useful for place holders

print(type(x))
