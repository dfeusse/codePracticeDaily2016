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
	return word

print vowel_indices("Mmmm")
print vowel_indices("Super")
print vowel_indices("Apple")