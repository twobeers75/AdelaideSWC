# gc_content
# base_count
# reverse_complement

"""class DNAstring:
	def __init__(self, string):
		self.string = string	

	def gc_content(self):
		#pass
		isUpper = self.upper()
		numG = isUpper.count('G')
		numC = isUpper.count('C')
		result = (numG + numC)/float(len(isUpper))*100
		return result

	def base_count(self, base):
		#pass
		isUpper = self.upper()
		if base.upper() == "A":
			baseCount = isUpper.count('A')
		elif base.upper() == "G":
			baseCount = isUpper.count('G')
		elif base.upper() == "C":
			baseCount = isUpper.count('C')
		elif base.upper() == "T":
			baseCount = isUpper.count('T')

		return isUpper.sequence.count(base)

	def reverse_complement(self):
		#pass
		basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

		letters = list(self) 
		letters.reverse()  
		letters = [basecomplement[base] for base in letters] 
		return ''.join(letters) 
"""
class NucleotideString:
	base_complement = {'G': 'C', 'C':'G',
                       'A': 'T', 'T': 'A'}
    
	def __init__(self, sequence):
		self.sequence = sequence
		self.bases = {}
    
	def base_count(self, base):
		if base in self.bases:
			return self.bases[base]
 		else:
			self.bases[base] = self.sequence.count(base)
			return self.bases[base]

	def gc_content(self):
		g = self.base_count('G')
		c = self.base_count('C')
		return float(g+c)/len(self.sequence)

	def reverse_complement(self):
		complement = ''        
		for base in self.sequence:
			complement = self.base_complement[base] + complement
		return complement

class DNAString(NucleotideString):
	pass

class RNAString(NucleotideString):
	base_complement = {'G': 'C', 'C':'G',
                       'A': 'U', 'U': 'A'}
