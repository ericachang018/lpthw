
#Created a function which takes in a cheese count, and a cracker count parameter
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count 
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man thats enough for a party!"
	print "Get a blanket. \n"

# Here we are feeding in the parameters directly. It is order sensitive
print "Can we just give the function numbers directly:"
cheese_and_crackers(20,30)

#Here we are assigning variables to our parameters 
print "or we can just use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50 

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# As you can see from the example below you can do math inside your parameters too using just plain intergers or varables and intergers
print "We can even do math inside too!"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +10000)


# Time to make my own fucntions 

def this_dumb_function(thingone, thingtwo, thingthree):
	some_addedthing = thingone + thingtwo 
	print some_addedthing
	print thingthree 
	print "wooh %d" % some_addedthing

this_dumb_function(1,9,3)


