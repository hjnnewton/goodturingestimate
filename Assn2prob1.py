class FileReader:
	def __init__(self, filename):
		# file objects are created by opening a file
		self.fileObj = open(filename, "r") # file object
		self.name = self.fileObj.name # file name
		self.dict1 = dict() # use a python dictionary
		self.dictfreq = {} # frequencies of frequencies
		self.dict1Size = 0 # keep track of dictionary size
	def readFile(self):
		"""" read() the file object """
		return self.fileObj.read()
	def closeFile(self):
		"""close the file"""
		self.fileObj.close()
	def buildDict(self):
		with self.fileObj as textfile:
			for line in textfile:
				value, key = line.split()
				self.dict1[key] = int(value)
				self.dict1Size = self.dict1Size +1
				# save the frequencies too
				if value in self.dictfreq:
					self.dictfreq[value] = self.dictfreq[value] +1
				else:
					self.dictfreq[value] = 1
		return self.dict1
	def dictSize(self):
		return self.dict1Size
	def getSingletonCount(self):
		# count the singletons
		count =0
		for key in self.dict1:
			if (self.dict1[key]==1):
				count = count+1
		return count


class GoodTuringEstimate:
	def __init__(self, filename):
		self.filereader = FileReader(filename)
		self.dict1 = self.filereader.buildDict()
		self.dict1Size = self.filereader.dictSize()
		self.singletons = list()
		self.singletoncount = 0
	def getDict1(self):
		return self.dict1
	def getDict1Size(self):
		return self.dict1Size
	def goodTuringEstimate(self):
		# add all singletons to a list
		for key in self.dict1:
			if (self.dict1[key]==1):
				self.singletons.append(key)
				self.singletoncount = self.singletoncount + 1
		print self.singletoncount, self.dict1Size
		# total probability of unseen words is N1/N
		return (self.singletoncount / float(self.dict1Size))*100
	def countNewWords(self, filename):
		filereader2 = FileReader(filename) # read this file
		dict2 = filereader2.buildDict() # build a dictionary from this text file
		newWordCount = 0 # number of words not previously encountered in part 1
		tokenCount = 0 # number of all new tokens
		# count all the tokens and new types from the part 2 frequency word list
		for key in dict2:
			tokenCount = tokenCount +1
			if key not in self.dict1:
				newWordCount = newWordCount +1
		print "new words:", newWordCount
		print "total new tokens: ", tokenCount
		return (newWordCount / float(tokenCount))*100



				

# TESTING:
if __name__ == "__main__":
	print "analyzing the concatenated file for part 1 of pieces"
	# populate dictionary of all word frequencies in part 1 texts
	allin1 = "part1/all_freq.txt"
	part1a = FileReader(allin1)
	part1a.buildDict()
	# do good turing estimate
	gte1 = GoodTuringEstimate(allin1)
	print "1a. the GTE probability of encountering a new word is ", gte1.goodTuringEstimate(), "%"

	# now count how many actual new words were found in the new part 2 texts
	allin2 = "part2/all_freq.txt"
	print "1b. the actual probability of encountering a new word is ", gte1.countNewWords(allin2), "%"
	
	# count how many singletons are in the combined tokenized text
	allin1and2 = "allin1and2_freq.txt"
	part1c = FileReader(allin1and2)
	part1c.buildDict()
	print "1c. the number of singletons in part 1 and part 2 combined is", part1c.getSingletonCount()

	# use the dictionary built in part1c, 
	gte1and2 = GoodTuringEstimate(allin1and2)
	allin3 = "part3/all_freq.txt"
	part1e = FileReader(allin3)
	print "1e. the actual probability of encountering a new word is ", gte1and2.countNewWords(allin3), "%"