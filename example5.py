import sys

reader = open('Pitching.csv', 'r')
line = reader.readline()
line = reader.readline()
numLines = 0
IPouts = 0

while line != '':
	numLines += 1
	lineList = line.split(',')
	value = lineList[12]
	IPouts += float(value) 
	line = reader.readline()

totalAverage = IPouts/numLines*100

print "total IPouts: " + str(IPouts) + ", line count: " + str(numLines) + ", total Av: " + str(totalAverage)




