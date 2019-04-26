# a method, also called a function is just a group of instructions
# that method can be referred to again and again

def doubler(someNumber):
	# print("Doubling: " + (str) someNumber)
	print(f"Doubling: {someNumber}")
	return someNumber * 2

myAnswer = doubler(2)

print(myAnswer)
	

