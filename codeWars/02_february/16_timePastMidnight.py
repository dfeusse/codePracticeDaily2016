'''
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to miliseconds.

Example:

past(0, 1, 1) == 61000
Note! h, m and s will be only Natural numbers! Waiting for translations and Feedback! Thanks!
'''
def past(h, m, s):
	# 1 m = 60,000 ms
	# 1 s = 1,000 ms
	return (s * 1000) + (m * 60000) + (h * 60000 * 60)

print past(0, 1, 1)

'''
def past(h, m, s):
    return (s + (m + h * 60) * 60) * 1000
    '''