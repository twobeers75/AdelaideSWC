
def test_dna_starts_with(dnaString1, dnaString2):
	'''check string starts with.

	>>> test_dna_starts_with('a', 'a')
	True
	>>> test_dna_starts_with('ACGTCGCTCG', 'ACGC')
	False
	'''	
	return dnaString1[0:len(dnaString2)]==dnaString2

if __name__ == '__main__':
	import doctest
	doctest.testmod()
