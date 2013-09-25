def countN(dnaString):
	isUpper = dnaString.upper()
	result = isUpper.count('N')
	return result

def GC(dnaString):
	isUpper = dnaString.upper()
	numG = isUpper.count('G')
	numC = isUpper.count('C')
	result = numG + numC#)/float(len(isUpper))*100
	return result

reader = open('example.fasta', 'r')
line = reader.readline()
numseqs = 0

while line != '':
	if line.startswith('>'):
		numseqs += 1
		tempLine = line.split(' ')
		seqID = tempLine[0]
		print seqID,
	else:
		GCcontent = GC(line)
		Ncontent = countN(line)
		print "Number of N's = " + str(Ncontent)
		print "GC Content = " + str(GCcontent / float(len(line) - Ncontent))

	line = reader.readline()

print "total number of seqs = " + str(numseqs)

