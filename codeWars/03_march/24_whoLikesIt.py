'''
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
'''
def likes(names):
	if len(names) == 0:
		return "no one likes this"
	elif len(names) == 1:
		return names[0] + " likes this"
	elif len(names) == 2:
		return names[0] + " and " + names[1] + " like this"
	elif len(names) == 3:
		return names[0] + ", " + names[1] + " and " + names[2] + " like this"
	else:
	 	return names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this"

print likes([]) #// must be "no one likes this"
print likes(["Peter"])# // must be "Peter likes this"
print likes(["Jacob", "Alex"])# // must be "Jacob and Alex like this"
print likes(["Max", "John", "Mark"])# // must be "Max, John and Mark like this"
print likes(["Alex", "Jacob", "Mark", "Max"])# // must be "Alex, Jacob and 2 others like this"

'''
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)
'''