'''
http://www.codewars.com/kata/5680781b6b7c2be860000036/train/python
We want to know the index of the vowels in a given word, for example, there are two vowels in 
the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

Some examples:
Mmmm  =&gt; []
Super =&gt; [2,4]
Apple =&gt; [1,5]
Note this is indexed from [1..n] (not zero indexed!)
'''
def vowel_indices(word):
	vowels = ['a','e','i','o','u']
	indice = []
	ind = 0
	for i in word:
		ind += 1
		if i.lower() in vowels:
			print i
			indice.append(ind)
	return indice

print vowel_indices("Mmmm")
print vowel_indices("Super")
print vowel_indices("Apple")

'''
def vowel_indices(word):
    return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']

def vowel_indices(word):
    lst = []
    for i, letter in enumerate(word.lower()):
        if letter in 'aeiouy':
            lst.append(i+1)
    return lst
 '''