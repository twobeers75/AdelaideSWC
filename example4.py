import sys

reader = open('pg76.txt', 'r')
line = reader.readline()
numLines = 0
lenLines = 0

#while line != '':
#	numLines = numLines + 1
#	lenLines = lenLines + len(line) 
#	line = reader.readline()
while line != '':
	numLines += 1
	lenLines += len(line) 
	line = reader.readline()

print "total length: " + str(lenLines) + ", line count: " + str(numLines)

#a = a + 1
#a += 1




