# There are several basic kinds of data that make up everything in Python

# Integers (Numbers without a decimal)
myInt = 17

# Floats or floating point numbers (Numbers with a decimal)
myFloat = 5.3

# Strings (A collection of text)
myString = "This is a String"
myString2 = 'So is this'
myString3 = 'This is how you show quotes inside a string "" '
myString4 = 'A backslash makes the interpreter handle the next character differently, \' '

# List (a collection that can be changed)
myList = [1, 2, 3, 4, 5, 6]


# Dict  (a collection of key:value pairs)
myDict = {"key": "value"}

# they can be printed
print(myList)
print(myDict)

# You can even access specific items within the collections

# With lists and strings you can refer to the items inside by their
# 'index' which is their position in the collection starting with 0


print(myList[0])
print(myString[0])

# You can even use a negative number to count from the other direction
# -1 refers to the last item in the list or string

print(myList[-1])


# Dictionaries work like you would expect a dictionary to
# If you want to know the definition of a word you look up the word
# So if you want a specific value from a dict you look up the key

print(myDict["key"])

