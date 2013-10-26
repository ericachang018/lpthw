#Exercise 15: Reading Files 
from sys import argv 
script, filename = argv 
# Open is a built in python function which will open files 
# pydoc open or http://docs.python.org/2/library/functions.html#open
txt = open(filename)
print "Here is your file %r" % filename 
print txt.read()
print "Type in the name of a new file to open:"
new_file = raw_input("> ")
new_text = open(new_file) 

# Earlier I made a mistake and wrote new_file.read() but you 
# can not do this as you will get an error saying that you
# can not preform the read function on a string. Remember 
# open the file first before it becomes a file object!!!
print new_text.read() 


