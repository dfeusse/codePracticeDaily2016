'''
http://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python
The input is a string str of digits. Cut the string into chunks of size sz (ignore the last 
	chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, 
reverse it; otherwise rotate it to the left by one position. Put together these modified chunks 
and return the result as a string.

If

sz is &lt;= 0 or if str is empty return ""
sz is greater (&gt;) than the length of str it is impossible to take a chunk of size sz hence return "".
Examples:
revrot("123456987654", 6) --&gt; "234561876549"
revrot("123456987653", 6) --&gt; "234561356789"
revrot("66443875", 4) --&gt; "44668753"
revrot("66443875", 8) --&gt; "64438756"
revrot("664438769", 8) --&gt; "67834466"
revrot("123456779", 8) --&gt; "23456771"
revrot("", 8) --&gt; ""
revrot("123456779", 0) --&gt; ""
'''
def revrot(string, sz):
	if sz == 0 or len(string) == 0 or sz > len(string):
		return ""
	nums = [int(i) for i in string]
	chunks = [nums[x:x+sz] for x in xrange(0, len(nums), sz)]
	if len(chunks[-1]) < sz:
		del chunks[-1]

	answer = []
	for i in chunks:
		temp = []
		for z in i:
			temp.append(z**3)
		if sum(temp) % 2 == 0:
			print '-----------'
			i.reverse()
			answer.append(i)
	return answer

print revrot("123456987654", 6) #--&gt; "234561876549"
print revrot("123456987653", 6) #--&gt; "234561356789"
print revrot("66443875", 4) #--&gt; "44668753"
print revrot("66443875", 8) #--&gt; "64438756"
print revrot("664438769", 8) #--&gt; "67834466"
print revrot("123456779", 8) #--&gt; "23456771"
print revrot("", 8) #--&gt; ""
print revrot("123456779", 0)