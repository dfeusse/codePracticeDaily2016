'''
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
Ignore numbers and punctuation.
'''
import string
# import ascii_lowercase

def is_pangram(s):
	'''
	for i in s.replace(" ",""):
		if i.lower() not in string.ascii_lowercase:
			print i.lower()
	'''

	alphabet = string.ascii_lowercase

	s = " ".join([i.lower() for i in s if not i.isdigit()])

	for c in string.punctuation:
		s = s.replace(c,"")

	s = " ".join(s).replace(" ","")

	#pone = [ i for i in s if i not in string.ascii_lowercase ]

	for i in s:
		if i in alphabet:
			# remove i
			alphabet = alphabet.translate(None, i)

	return False if len(alphabet) > 0 else True

#print is_pangram("The quick brown fox jumps over the lazy dog!")
print is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ")
print is_pangram("This isn't a pangram!")

'''
def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

 import string

def is_pangram(s):
    s = s.lower()
    return all(letter in s for letter in string.lowercase)

def is_pangram(s):
    s = s.lower()
    for token in string.ascii_lowercase:
        if token not in s:
            return False
    return True

'''