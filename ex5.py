#Exercise 5 More Variables and Printing
#In this exercise we will be learning how to embed Variables into our strings
#This is useful so you dont have to "break your" strings "appart" for a Variable
#Instead you can do this "break your %s appart" % string 
#Common String Formatting Objects 
# %s = String converts python object using str()
# %r = String converts python object using repr()
# %d = Signed interger decimal 

# For more on String Formatting operations view the Python Doc 
# http://docs.python.org/2/library/stdtypes.html  5.6.2

name = "Erica Chang" # Sorry Zed Shaw this exercise is about me today 
age = 26  
height = 66 #inches I think this is right
weight = 115 
eyes = "Brown"
teeth = "White" # i hope
hair = "Black and blue"

print "Let's talk about %s" % name 
print "She thinks she is  %d inches tall." % height
print "She is %d pounds but shhh thats a secret" % weight
print "Actually thats not too heavy and its on the internet so not a secret"
print "She got %s eyes and %s hair." %(eyes, hair)
print "Her teeth are usually %s depending on the coffee" % teeth

print "If I add %d, %d, and %d I get %r." %(age,height,weight,age+height+weight) 

