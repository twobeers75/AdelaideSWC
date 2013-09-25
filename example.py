import sys

myList = sys.argv[1:]
myList.sort()
myFirstString = ', '.join(myList[:-1])
print (myFirstString.title() + " and " + myList[-1].title() + ".")

