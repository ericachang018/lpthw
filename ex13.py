# Exercise 13: Parameters Unpacking, Variables 
# This is a cool modual that will let you read in parameters when you run the program
# to run this script you will type the following in the terminal 
# >> python ex14.py variable_one var_2 three 
# your variables can be anything you want them to be. =D wooh! Nifty yea! 
from sys import argv 

# set your arguments (similar to paramters in a function) here! 
script, first, second, third = argv 

print "The script is called:", script 
print "The first variable is:", first
print "The second variable is:", second 
print "The third variable is:", third 


