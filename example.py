import sys

# The first example from the workshop which takes an argument from the user
myList = sys.argv[1:]
myList.sort()
myFirstString = ', '.join(myList[:-1])
print (myFirstString.title() + " and " + myList[-1].title() + ".")

