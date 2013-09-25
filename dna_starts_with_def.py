"""import sys

myList = sys.argv[1:]
if myList[0].startswith(myList[1]):
	print 'True'
else:
	print 'False'
"""
def dna_starts_with(dnaString1, dnaString2):	
return dnaString1[0:len(dnaString2)]==dnaString2

passes = 0	
for (i, (seq, prefix, expected)) in enumerate(test):	
	if dna_starts(seq, prefix) == expected:	
		passes += 1	
	else:	
		print('test %d failed' % i)	
	
	print('%d/%d tests passed' % (passes, len(test)))


