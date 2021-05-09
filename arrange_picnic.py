allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
	'Bob': {'ham sandwiches': 3, 'apples': 2},
	'Carol': {'cups': 3, 'apple pies': 1}}
# To write more elegant codes, we are required to indent appropriately.
def totalBrought(guests,item):
	# Create a function with two attributes.
	# In which 'guests' indicates the collection of guests and their demands.
	numBrought=0
	# To set initial value at 0. 
	for k,v in guests.items():
		numBrought=numBrought+v.get(item,0)
	# 'k' iterates from 'Alice' to 'Carol'
	# 'v' iterates from the demand from Alice to Carol. 
	return numBrought
	#The ultimate answer for this funtion would be numBrought,
	#given the two attributes. 
apple_count=totalBrought(allGuests,'apples')
print(apple_count)

print('Number of things being brought:')
print(' - Apples '+str(apple_count))
# The above method is called concatenation of strings.
# Such as:
print('My name is '+'Suzuha')
# But concatenation can only be used in all-string scenarios.
print(f" - Apples {apple_count}")
# Another way to get the same result as concatenation.