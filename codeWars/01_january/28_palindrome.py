'''
create a reverse function, use it for palindrome
'''
def palindrome(string):
	return string == string[::-1]

print palindrome('ana')