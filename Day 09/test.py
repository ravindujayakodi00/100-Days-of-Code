# Define a dictionary
dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
}

# Retrieve items from  a dictionary
# print(dictionary["Bug"])
# print(dictionary["Function"])

# Add Items to Dictionary
dictionary["Loop"] = "The action of doing something over and over again."

# print(dictionary)

# empty_dictionary = {}
#
# empty_dictionary["Name"] = "Ravindu Jayakodi"
#
# print(empty_dictionary)

for key in dictionary:
    print(key + ":")
    print(dictionary[key])
