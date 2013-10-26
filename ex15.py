# Exercise 15: Reading Files 
# To run this program type 
# >> python ex15.py ex15_sample.txt 
# when the script prompts you for another file to open 
# you can type in ex15_more.txt or any other file you want open

# ^__^ http://docs.python.org/release/2.5.2/lib/bltin-file-objects.html
# More http://docs.python.org/2/tutorial/inputoutput.html:


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

# Now I'm going to close my files since thats good practice 
txt.close()
new_text.close() 
