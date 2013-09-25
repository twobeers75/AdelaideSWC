import sys

input_string = 'CACGAGTAGCTAGTAGCTAGTAGCTGATCGATCTACGTACGTACGTACGTACGTACGTAGCTACGTACGTAGC'

isLower = input_string.lower()
numA = isLower.count('a')
numG = isLower.count('g')
numC = isLower.count('c')
numT = isLower.count('t')
my_dict = {'A': numA , 'G': numG , 'C' : numC , 'T' : numT }

myGC = (numG + numC)/float(len(isLower))*100

print my_dict
print myGC
