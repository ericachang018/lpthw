#Exercise 32 Lists and Loops 

# Our lists! 
the_count = [1,2,3,4,5,]
fruits = ['apples', 'oranges','apples','grapes','pears']
change = [1, 'pennies', 2, 'dimes',3 ,'quarters']


# This will loop though our list of stuff and print things 
# for each item in the list. 
for number in the_count:
	print "This is the count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit 

for i in change:
	print "I got %r" %i 

# we can make an empty list and add shit to it 
elements = []

# This shouldn't print since there is nothing in the list to loop though
for i in elements:
	print "there should be nothing in here but if there is we will print this lots of times"

# add shit
for i in range(0,6):
	print "Adding %d to the list" %i 
	elements.append(i) 

# now we can print out the items we just added to our empty list
# to make sure it worked 


