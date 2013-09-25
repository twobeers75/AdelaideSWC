def removeN(dnaString):
	isUpper = dnaString.upper()
	result = isUpper.replace('N','')
	return result

def GC(dnaString):
	isUpper = dnaString.upper()
	numG = isUpper.count('G')
	numC = isUpper.count('C')
	result = (numG + numC)/float(len(isUpper))*100
	return result

tempdna = removeN('NNNNNNNNNNNNNNNNNNnnnNNNNNNNNAAGGGGGGGG')
print GC(tempdna)
