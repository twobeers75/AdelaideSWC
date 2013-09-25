import sys

myList = sys.argv[1:]
if myList[0].startswith(myList[1]):
	print 'True'
else:
	print 'False'

