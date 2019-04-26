myName = "Michael DiCicco"
letters = []

# for i in range(15):
#     print(myName[i])

# This is the same as the following except it only works if myName is of length 15
# The following works for a myName of any length

for i in range(len(myName)):
    print(myName[i])

print()
# What if I wanted to change the i's to something else like "!"'s?

for i in range(len(myName)):
    if myName[i] == 'i':
        print('!')
    else:
        print(myName[i])
	
# of course it would be easier/better to use the built in string method replace

print(myName.replace('i','!'))
print(myName)

for letter in myName:
	letters.append(letter)

print(letters)
