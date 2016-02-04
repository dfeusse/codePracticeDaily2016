'''
http://www.codewars.com/kata/55ea5650fe9247a2ea0000a7/train/python
The string given to your function has had an "egg" inserted directly after each consonant. 
You need to return the string before it became eggcoded.

example:

unscrambleEggs("Beggegeggineggneggeregg"); => Beginner

Kata is supposed to be for beginners to practice regular expressions, so commenting would be appreciated.
Fundamentals
'''
def unscramble_eggs(word):
	return word.replace("egg", "")

print unscramble_eggs("Beggegeggineggneggeregg")

'''
def unscramble_eggs(word):
    return word.replace('egg','')

from re import sub
def unscramble_eggs(word):
    # Geggoodegg Legguceggkegg!
    return sub(r'([^aieou])egg',r'\1', word)
'''