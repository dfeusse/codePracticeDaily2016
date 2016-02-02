'''
Given an array of integers of any length, return an array that has 1 added to the value 
]represented by the array.

For example an array [2, 3, 9] equals 239, add one would return an array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

The array can't be empty and only positive, single digit integers are allowed. The function should 
return null if the array is empty or any of the array values are negative or more than 10.

[1, -9] would return null/nil/None (according to the language implemented).
'''
def up_array(arr):
	if len(arr) == 0:
		return None
	for i in arr:
		if (i < 0) or (i > 9):
			return None
	newInt = str(int("".join(map(str, arr))) + 1)
	return [int(i) for i in newInt]

print up_array([1, -9])
print up_array([4, 3, 2, 5])
print up_array([2, 3, 9])
print up_array([])
print up_array([2, 3, 19])

'''
def up_array(arr):
    return None if arr==[] or any([x not in range(10) for x in arr]) else [int(c) for c in str(int("".join([str(x) for x in arr]))+1)]

def up_array(arr):
  if not arr or min(arr) < 0 or max(arr) > 9:
    return None
  else:
    return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
'''