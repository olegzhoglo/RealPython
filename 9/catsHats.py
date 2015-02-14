catsInHats = {}
catsWithoutHats = {}

#controls walking in a circle 100 times, returns final list of cats
def walkCircle():
	for r in range(1,101):
		walkThroughCats(r)
	return catsInHats.keys()

#selects what cat to look at next depending on what round it is
def walkThroughCats(iterator):
	nextCat = 0
	while nextCat < 100:
		nextCat = nextCat + iterator
		if nextCat < 100:
			testCat(nextCat)
		else:
			continue

#tests if cat already has a hat
def testCat(cat):
	if cat in catsInHats:
		removeHat(cat) 
	else:
		placeHat(cat)

#adds hat to cat
def placeHat(cat):
	catsInHats[cat] = "hat"

#removes hat from cat
def removeHat(cat):
	del(catsInHats[cat])

print(walkCircle())