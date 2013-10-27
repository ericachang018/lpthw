# Exercise 16: Reading and Writing files. 
# This exercise will use the same sample text file from the previous exercise. 
# To run this program >> python ex16.py ex15_sample.txt will be used. 

from sys import argv
script, filename = argv

print "We're going to erase %r." % filename 
print "If you don't want that, hit CTRL - C (^C)."
print "If you do want that hit RETURN." 

raw_input("?")

print "Opening file..." 
# using the w signifieds that you are opening a write file. The format is open(filename, mode) some of the different modes are 'r' read only 'w' write only  'a' appending to the end of a file 'r+' is reading and writing 
target = open(filename, 'r+')
print "lets read our file before we toss it away and write some new junk to it"
print target.read()

#truncate is not needed because 'w' mode will erase an exisiting file with the same name. But since i'm using r+ mode it will append to the end so I will continue to use the truncate method in order to clear out my file! 
 
print "Truncating the file. Goodbye" 
target.truncate(0)

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file" 

# http://stackoverflow.com/questions/8691311/python-how-to-write-multiple-strings-in-one-line 
# In order to write this in one line what I did was told my program to write one big string. In my string I have some string formatters and line breaks. I made some of hte same mistakes as the stack overflow examples which is why I included the artical which helped get me unstuck. 

target.write('%s\n%s\n%s\n' %(line1, line2, line3)) 

# The following can be deleted but is kept for learning and looking back at. 
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
print "now lets read our file to check that the changes have been made"

#I got a little stuck here because it took a little trial and error to figure out that after writing to a file you need to re open it again in order for python to read the changes you made. 
target = open(filename)
print target.read()
target.close()
print"And finally, we close it."
print"goodbye!"	
