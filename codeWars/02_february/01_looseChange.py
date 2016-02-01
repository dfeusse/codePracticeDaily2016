'''
Loose Change

Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, 
and returns a dictionary which shows the least amount of coins used to make up that amount.
 The only coin denominations considered in this exercise are: Pennies (1), Nickels (5), Dimes (10
 and Quarters (25). Therefor the dictionary returned should contain exactly 4 key/value pairs.

loose_change(56)  {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
A couple notes regarding expected behavior:

If the function is passed either 0 or a negative number, the function should return the dictionary 
with all values equal to 0.

loose_change(-435)   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
If a float is passed into the function, its value should be be rounded down, and the resulting 
dictionary should never contain fractions of a coin.

loose_change(4.935)    {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
'''
import math

def loose_change(change):
    answer = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if change <= 0:
        return answer
    if isinstance(change, int) != True:
        change = math.floor(change)
    print change
    if change/25>=1:
        answer['Quarters'] = math.floor(change/25)
        change = change - (change/25 * 25)
    if change/10>=1:
        answer['Dimes'] = math.floor(change/10)
        change = change - (change/10 * 10)
    if change/5>=1:
        answer['Nickels'] = math.floor(change/5)
        change = change - (change/5 * 5)
    if change/1>=1:
        answer['Pennies'] = math.floor(change/1)
        change = change - (change/1 * 1)
    return answer
	

print loose_change(56)
print loose_change(66)
print loose_change(-435)
print loose_change(3.9)#, {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})
print loose_change(12.6)

'''
import math

def loose_change(cents):
    if cents < 0:
        cents = 0
    cents = int(cents)
    
    change = {}

    change['Quarters'] = cents // 25
    cents = cents % 25

    change['Dimes'] = cents // 10
    cents = cents % 10

    change['Nickels'] = cents // 5
    cents = cents % 5
    
    change['Pennies'] = cents
    
    return change


def loose_change(cents):

    total_cents = 0
    
    denomination_list = [ ["Quarters", 25],
                          ["Dimes", 10],
                          ["Nickels", 5],
                          ["Pennies", 1] ]
    
    change_dict = {}
    
    for denomination in denomination_list:
    
        coin_count = 0
            
        while total_cents + denomination[1] <= cents:
        
            total_cents += denomination[1]
            coin_count += 1
            
        change_dict [denomination [0]] = coin_count

    return change_dict
'''