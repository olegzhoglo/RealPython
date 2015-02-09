from capitals import capitals_dict
import random

def getCapital():
	state = random.choice(capitals_dict.keys()) #select random key
	capital = capitals_dict[state] #get capitol

	return state, capital

def userInteraction():
	userInput = ""
	while True:
		stateCapitalPair = getCapital()
		state = stateCapitalPair[0]
		capital = stateCapitalPair[1]
		answer = raw_input("What is the capital of " + str(state) + "? ")
		if answer == "exit" or answer == "Exit" or answer == "EXIT":
			break
		elif answer == capital or answer == str.lower(capital):
			print("Correct!")
		else:
			print("Wrong!")

userInteraction()




