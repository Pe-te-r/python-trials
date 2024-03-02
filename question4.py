"""Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string."""

def capitalize_word(sentense):
    return sentense.title()

print("Enter the sentense you want to capitalize words\n")
sentense=input(">> ")

print(capitalize_word(sentense))
