'''
Write a function that removes each 9 that it is in between 7s.

seven_ate9('79712312') =&gt; '7712312'
seven_ate9('79797') =&gt; '777'
'''
def seven_ate9(string):
	array = [int(i) for i in string]
	indexOfArray = 0
	badd = []
	for i, element in enumerate(array):
		if i > 0 and i < len(array)-1:
			if element == 9 and array[i-1] == 7 and array[i+1] == 7:
				badd.append(i)

	for i in sorted(badd, reverse=True):
		print i
		del array[i]
	return ''.join(str(i) for i in array)

print seven_ate9('79712312') #=&gt; '7712312'
print seven_ate9('79797') #=&gt; '777'