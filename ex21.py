# Functions can return stuff! 

def add(a,b): 
	print "Adding %d + %d " %(a,b)
	return a + b 

def subtract (a,b): 
	print "Subtracting %d - %d" % (a,b)
	return a - b 

def multiply (a,b): 
	print "Multiplying %d * %d" % (a,b)
	return a * b 

def divide (a,b): 
	print "Dividing %d / %d" %(a,b)
	return a/b

print "Let's do some math with just functions!"

age =  add(30,5)
height = subtract (78,4)
weight = multiply(90,2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

#puzzle for extra credit!!

print "Here's a puzzle"
#  Yes i can! 50 / 2 = 25 
#  25 * 180 = 4500
#  74 - 4500 = - 4428
#  35 + 4428 = - 4391 vs -4393 humm off by a few... 

what = add(age, subtract(height,multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do that by hand?"


