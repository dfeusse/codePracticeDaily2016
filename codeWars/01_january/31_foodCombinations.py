'''
Given an array containing a list of good foods, return a string containing the assertion 
that any two of the individually good foods are really good when combined.

eg: "You know what's actually really good? Pancakes and relish."

Examples:

Good_foods = ["Ice cream", "Ham", "Relish", "Pancakes", "Ketchup", "Cheese", "Eggs", "Cupcakes", 
"Sour cream", "Hot chocolate", "Avocado", "Skittles"]

actually_really_good( Good_foods ) #  "You know what's actually really good? Pancakes and relish."

actually_really_good( ['Peanut butter'] ) #  "You know what's actually really good? Peanut butter 
and more peanut butter."

actually_really_good( [] ) #  "You know what's actually really good? Nothing!"
Notes:

There are many different valid combinations of 2 foods it doesn't matter which one you choose.
But there should be 2 different foods listed unless there was only one food given in the input 
array.
Capitalization should be correct, the first given food should be capitalized, but the second 
should not.
The input array should not be modified by the method.
'''
import random

def actually_really_good(array):
	responseStem = "You know what's actually really good? "
	lenArgument = len(array)
	if lenArgument == 0:
		return responseStem + 'Nothing!'
	elif lenArgument == 1:
		return responseStem + array[0].capitalize() + ' and more ' + array[0].lower() + '.'
	else:
		random.shuffle(array)
		return responseStem + array[0].capitalize() + ' and ' + array[1].lower() + '.'


Good_foods = ["Ice cream", "Ham", "Relish", "Pancakes", "Ketchup", "Cheese", "Eggs", "Cupcakes", 
"Sour cream", "Hot chocolate", "Avocado", "Skittles"]

print actually_really_good( Good_foods ) #  "You know what's actually really good? Pancakes and relish."
print actually_really_good( ['Peanut butter'] ) #  "You know what's actually really good? Peanut butter and more peanut butter."
print actually_really_good( [] ) #  "You know what's actually really good? Nothing!"
print actually_really_good(['fish fingers','custard'])
print actually_really_good(['Fish Fingers','Custard'])
print actually_really_good(['fish Fingers','cUstard', 'sENAPE'])

'''
OUTPUT = 'You know what\'s actually really good? {}'.format


def actually_really_good(foods):
    foods = list(set(foods))
    length = len(foods)
    if length == 0:
        return OUTPUT('Nothing!')
    return OUTPUT('{} and more {}.'.format(
        foods[0].capitalize(), foods[0 if length == 1 else 1].lower()))
'''