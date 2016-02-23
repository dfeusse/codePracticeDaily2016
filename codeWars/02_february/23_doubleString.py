'''
http://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
Given a string, you have to return a string in which each charcter (case-sensitive) is repeated once.
'''
def double_char(s):
	return ''.join([i*2 for i in s])

print double_char("String")# ==> "SSttrriinngg"
print double_char("Hello World") #==> "HHeelllloo  WWoorrlldd"
print double_char("1234!_ ") #==> "11223344!!__  "

'''
def double_char(str):
    return "".join(ch+ch for ch in str)
'''