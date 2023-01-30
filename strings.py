
#Strings

# single_quotes = 'Look single quotes'
# double_quotes = "Look double quotes"
#
# print(single_quotes)
# print(double_quotes)

# string_failure = 'I said 'Wow''
# print(string_failure)

# escape_example = 'I said \'Wow\'' # called escape character
# print(escape_example)

# quote_in_quote ='I said "Wow!"'
# print(quote_in_quote)

# reverse_quote = "I said 'WOW!'" # BEST ONE TO USE!!!!!!!!!!!!!!!!!!!
# print(reverse_quote)

# --------String Slicing
#Everything in code starts with 0 not 1
# H E L L O   W O R L D ! ||||||||SPACES ARE NUMBERS AS WELL
# 0 1 2 3 4 5 6 7 8 9 10
#
# hw = "Hello World!"
#
# print(hw[7:])
# print(hw[-5:]) # : colon will make it mean anything up until after that point.#
# print(hw[:5])  # : colon will make it mean anything up until after that point
# print(hw[0:5]) # we are slicing strings up

# String Methods

# strip: removes all white space
#
# white_space = "lot's of space at the end                                   "
# print(len(white_space)) #59
# print(len(white_space.strip()))
#
# # A few more
#
# example_text = "Here's a decent amount of text. Yep!!!!!!!!! text"
#
# # Counts a substring within a string.
# print(example_text.count("text")) #2
#
# # Makes everything lower case
# print(example_text.lower())
#
# #Make everything uppercase
# print(example_text.upper())
#
# # Capitilase things/ Only first letter
# print(example_text.capitalize())
#
# #Replace character/text
# print(example_text.replace("amount", "number")) # see the replacement
#
# # Concatenation

# a = "here "
# b = "more " # remeber to add spaces
# c = "much more"
#
# print(a + b + c)

# # Casting // Converts one data type into another one.
# x = 2
# y = 5.4
# z = " there's a  number 25.4 unless we put a space!"
#
# # print(x + y + z)
#
# print(str(x) + str(y) + z)
#
# # String to numeric
#
# int_string = "6"
#
# print(float(int_string))
# print(type(float(int_string)))

#-------- F - String; Allows us not to have to cast everything and have to change it to str/int/float
# etc....

# name = "Lassie"
# years = 6
# height_cm = 65.9
#
# print(f"{name} is {years} years old and {height_cm} cm tall.")

# F - Strings allows us to use Methods/Evaluations  as well

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS!!!!!!!")

#F - Strings to round up and specify precision and decimals

pi = 3.14159265359

print(f"Pi to 3 decimal places: {pi:.3f}") # this for how many decimal places
print(f"Pi to 3 decimal places: {pi:.5f}")

score = 16
max_score = 26

print(f"You scored {score / max_score}") #0.6153846153846154
print(f"You scored {score / max_score:%}") # 61.538462% turns it in to a percentage
print(f"You scored {score / max_score:.2%}") #61.54%
print(f"You scored {score / max_score:.0%}") #62%