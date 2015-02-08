import random

def makePoem():
	nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
	verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
	adjectives = ["furry" , "funny" , "pink", "incredulous", "fragrant", "exuberant", "glistening"]
	prepositions = ["against" , "after" , "into" , "beneath", "upon", "for", "in", "like", "over", "within"]
	adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

	selectedNouns = []
	selectedVerbs = []
	selectedAdjectives = []
	selectedPropositions = []
	selectedAdverb = []

	#add 3 nouns
	while len(selectedNouns) < 3:
		word = random.choice(nouns)
		
		if word not in selectedNouns:
			selectedNouns.append(word)
		else:
			continue

	#add 3 verbs
	while len(selectedVerbs) < 3:
		word = random.choice(verbs)
		
		if word not in selectedVerbs:
			selectedVerbs.append(word)
		else:
			continue

	#add 3 adj
	while len(selectedAdjectives) < 3:
		word = random.choice(adjectives)
		
		if word not in selectedAdjectives:
			selectedAdjectives.append(word)
		else:
			continue

	#add 2 preps
	while len(selectedPropositions) < 2:
		word = random.choice(prepositions)
		
		if word not in selectedPropositions:
			selectedPropositions.append(word)
		else:
			continue

	#add 1 adverb
	while len(selectedAdverb) < 1:
		word = random.choice(adverbs)
		
		if word not in selectedAdverb:
			selectedAdverb.append(word)
		else:
			continue
		
	title = "{} {} {}".format(aChooser(selectedAdjectives[0]), selectedAdjectives[0], selectedNouns[0])
	line1 = "{} {} {} {} {} the {} {}".format(aChooser(selectedAdjectives[0]), selectedAdjectives[0], selectedNouns[0], selectedVerbs[0], selectedPropositions[0], selectedAdjectives[1], selectedNouns[1])
	line2 = "{} , the {} {}".format(selectedAdverb[0], selectedNouns[0], selectedVerbs[1])
	line3 = "the {} {} {} {} {} {}".format(selectedNouns[1], selectedVerbs[2], selectedPropositions[1], aChooser(selectedAdjectives[2]), selectedAdjectives[2], selectedNouns[2])

	#return poem 
	return title, line1, line2, line3

#choose A or An
def aChooser(adjective):
	word = adjective
	vowels = ["a","e","i","o","u"]
	if word[0] in vowels:
		return "an"
	else:
		return "a"


poem = (makePoem())

for i in poem:
	print(i)




