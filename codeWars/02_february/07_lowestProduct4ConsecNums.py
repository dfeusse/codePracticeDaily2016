'''
http://www.codewars.com/kata/554e52e7232cdd05650000a0/train/python
Create a function that returns the lowest product of 4 consecutive numbers in a given string of numbers.

This should only work is the number has 4 digits of more. If not, return "Number is too small".

Example

lowest_product("123456789")--&gt; 24 (1x2x3x4)
lowest_product("35") --&gt; "Number is too small"
'''
def lowest_product(num):
	if len(num) < 4:
		return "Number is too small"
	nums = [int(i) for i in num]
	answer = 1000000000
	for i, integer in enumerate(nums):
		if len(nums) - (i+4) >= 0: 
			product = nums[i] * nums[i+1] * nums[i+2] * nums[i+3]
			if product < answer:
				answer = product
	return answer

print lowest_product("123456789")
print lowest_product("35")
print lowest_product("")
print lowest_product("3512")

'''
def lowest_product(input):
    length = len(input)
    
    if length < 4:
        return "Number is too small"
    
    def muller(fourchar):
        prod = 1
        for num in fourchar:
            prod *= int(num)
        return prod
        
    return min([muller(input[i:i+4]) for i in range(length-3)])

from operator import mul

def lowest_product(input):
    return min(reduce(mul, (int(d) for d in input[i : i + 4])) for i in xrange(len(input) - 3)) if len(input) >= 4 else "Number is too small"
    '''