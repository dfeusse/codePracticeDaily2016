'''
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''
def find_it(seq):
	if isinstance(seq, list):
		for i in seq:
			if seq.count(i) % 2 != 0:
				return i
	else:
		return None

print find_it("Example")
print find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])#, 5)

'''
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

from collections import Counter
def find_it(l):
    return [k for k, v in Counter(l).items() if v % 2 != 0][0]
'''