def nucleotideContent(dnaString):	
	'''This function must return the contribution	
	of nucleotides ATCG (as uppercase) from a given DNA 	
	string inside a dictionary, where each key refers to	
	a nucleotide	
	'''	
	dnaDict = {}	
	uniques=set(dnaString)	
	for nucleotide in uniques:	
		dnaDict[nucleotide]=dnaString.count(nucleotide)	
	
	return dnaDict

# Tests in table	
# Sequence Expected
Tests = [	
['ACGTGT', {'A': 1, 'C': 1, 'G': 2, 'T': 2}],
['CAGGTT', {'A': 1, 'C': 1, 'G': 2, 'T': 2}],
['ACGZGT', {'A': 1, 'C': 1, 'G': 2, 'T': 2}],
['acgzgt', {'A': 1, 'C': 1, 'G': 2, 'T': 2}],
]

# Run and report    
passes = 0    
for (i, (seq, expected)) in enumerate(Tests):    
	if nucleotideContent(seq) == expected:    
		passes += 1    
	else:    
		print('test %d failed' % i)    
    
print('%d/%d tests passed' % (passes, len(Tests)))

	



