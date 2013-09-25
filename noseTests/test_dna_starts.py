
def test_dna_starts_with(dnaString1, dnaString2):	
	return dnaString1[0:len(dnaString2)]==dnaString2


# Tests in table	
# Sequence Prefix Expected
 
Tests = [	
['a', 'a', True],
['at', 'a', True],
['at', 'at', True],
['at', 't', False],
]	

# Run and report    
passes = 0    
for (i, (seq, prefix, expected)) in enumerate(Tests):    
	if test_dna_starts_with(seq, prefix) == expected:    
		passes += 1    
	else:    
		print('test %d failed' % i)    
    
print('%d/%d tests passed' % (passes, len(Tests)))

