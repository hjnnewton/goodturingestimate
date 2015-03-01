import random

class processEmma:
	def __init__(self):
		self.filename = "emma_sentences_nopunct.txt"
		self.fileObj = open(self.filename, "r") # file object
		self.fileStr = ""

	def parseSentences(self):
		with self.fileObj as textfile:
			for line in textfile:
				self.fileStr = self.fileStr+" start "+line+" end"
		return self.fileStr

class nGramsEmma:
	def __init__(self):
		self.filename = "emma_sentences_final.txt"
		self.fileObj = open(self.filename, "r") # file object
		self.dict = dict()
		self.fileStr = ""

	def getString(self):
		with self.fileObj as textfile:
			for line in textfile:
				self.fileStr = line
		return self.fileStr

	def buildDict(self):
		# split into a list of tokens
		tokens = self.fileStr.split()
		size = len(tokens)

		# for each token
		for i in range(0,size-2):
			# if the key isn't already in the self.dict, add a dictionary for it
			currentT = tokens[i]
			nextT = tokens[i+1]
			if currentT not in self.dict:
				self.dict[currentT] = dict()
				# and add the next token in as an entry, along with its count
				self.dict[currentT][nextT] = 1
			# if the key is already in the self.dict, check if its value (dictionary) is there
			else:
				# if the next token isn't a value for this current token's dictionary, add it
				# and increment the count to 1
				if nextT not in self.dict[currentT]:
					self.dict[currentT][nextT] = 1
				# if the next token WAS a value for this current token's dictionary, increment the count
				else:
					self.dict[currentT][nextT] = self.dict[currentT][nextT]+1

		for key in self.dict:
			#print key
			valuecount = 0
			# first find out how many values are stores for this key
			for value in self.dict[key]:
				valuecount = valuecount +1
			# then update the percentages for the values
			for value in self.dict[key]: 
				#print "     ", value
				self.dict[key][value] = (self.dict[key][value] / float(valuecount))
				#print "           ", self.dict[key][value]
			# then make a cumulative frequency for the values
			prev = 0.0
			for value in self.dict[key]:
				self.dict[key][value] = prev + self.dict[key][value]
				#print "c            ", self.dict[key][value]
				prev = self.dict[key][value]

		# finally, add a value and frequency for [finis]
		self.dict["finis"] = dict()
		self.dict["finis"]["."] = 1.0

	def genSentence(self):
		# start with start
		sentence = ""
		firstWord = "start"
		currentWord = firstWord
		# for each word that has been known to follow the current word
		while currentWord is not ".":
			# if the current Word is end,concatenate and return
			if (currentWord == 'end'):
				sentence = sentence +" "+ currentWord
				return sentence
			else:
				sentence = sentence + " " + currentWord
				# find the max val
				maximum = self.findMax(currentWord)
				# get a random float between 0 and max
				rand = random.uniform(0.0, maximum)
				newkey = self.findKey(currentWord, rand)
				currentWord = newkey

	# for a key, find the maximum cumulative frequency
	# this should equal one but something is wrong
	def findMax(self, key):
		maxval = 0
		for v in self.dict[key]:
			if self.dict[key][v] > maxval:
				maxval = self.dict[key][v]
		return maxval

	def findKey(self, key, rand):
		for v in self.dict[key]:
			# if the random value is between the previous v and the next v, return this v
			if rand < self.dict[key][v]:
				return v



# TESTING
if __name__ == "__main__":
	test = processEmma()
	test.parseSentences()

	ngram = nGramsEmma()
	ngram.getString()
	ngram.buildDict()

	for i in range(0,10):
		print ngram.genSentence()