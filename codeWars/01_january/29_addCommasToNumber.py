'''
http://www.codewars.com/kata/56a115cadb39a2faa000001e/train/python
Add commas to a number

Your task is to convert a given number into a string with commas added for easier readability. 
The number should be rounded to 3 decimal places and the commas should 
be added at intervals of three digits before the decimal point. 
There does not need to be a comma at the end of the number.

You can be passed both positive and negative numbers.

For example:

commas(1) == "1"

commas(1000) == "1,000"

commas(100.2346) == "100.235"

commas(1000000000.23) == "1,000,000,000.23"

commas(-1) == "-1"

commas(-1000000.123) == "-1,000,000.123"
'''
def commas(num):
	#new = "{:,}".format(num)
	pone = '%.12g' % num
	print pone
	if isinstance(num, int):
		s = str(num)
		new = s.rstrip('0').rstrip('.') if '.' in s else s
		return "{:,}".format(num)
		#return "{:,}".format(new)
	else:
		return "{:,}".format(round(num,3)) 

print commas(1)# == "1"
print commas(1000)# == "1,000"
print commas(100.2346)# == "100.235"
print commas(1000000000.23)# == "1,000,000,000.23"
print commas(-1)# == "-1"
print commas(-1000000.123)# == "-1,000,000.123"
print commas(-2000.0)