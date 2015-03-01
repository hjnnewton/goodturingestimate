import random

class SentenceGen:
	def __init__(self):
		self.freqs = dict()

	def populateFreqs(self):
		# the probability that buffal happens after start
		self.freqs["start"] = dict()
		self.freqs["start"]["buffalo"] = 1.0
		self.freqs["buffalo"] = dict()
		self.freqs["buffalo"]["buffalo"] = 0.6
		self.freqs["buffalo"]["end"] = 0.4
		self.freqs["end"]= dict()
		self.freqs["end"]["."] = 1.0

	def genSentence(self):
		# start with start
		sentence = ""
		firstWord = "start"
		currentWord = firstWord
		# for each word that has been known to follow the current word
		while currentWord is not ".":
			if currentWord in self.freqs:
				for word in self.freqs[currentWord]:
					sentence = sentence + currentWord
					randomKey =  random.choice(self.freqs[currentWord].keys())
					# concatenate sentenc
					currentWord = randomKey
			else:
				sentence = sentence + "end"
		return sentence

# TESTING
if __name__ == "__main__":
	# build the dictionary of dictionaries
	test = SentenceGen()
	test.populateFreqs()
	# generate a sentence 10 times
	for i in range(0,10):
		print test.genSentence()
