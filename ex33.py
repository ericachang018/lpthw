# while loops 
i = 0 

numbers = []

# This will added numbers 1 to 6 to our empty list and stop when i becomes greater than 6
# it will also print out a status along the way so you know what it is doing. 
while i < 6: 
	print "at the top i is %d" % i
	numbers.append(i)
	i = i + 1 
	print "Numbers now:" , numbers
	print "at the bottem i is %d " %i 
print "The numbers:"

# for loop printing out all the numbers in numbers list that we just added
for num in numbers: 
	print num 
