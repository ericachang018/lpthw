# exercise 38 doing more things to lists
ten_things = "one thing two thing three thing more"
print "Wait there's not 10 things in a list, they are a string, Lets fix that."

stuff = ten_things.split(" ")
more_stuff= ["Day", "Night", "Song", "corn","bananna", "frisbee"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "there's %d items now" % len(stuff)

print "There we go: ", stuff
print  "lets do more stuff with stuff"
# This will access the second item in the list
print stuff[1]
# this will access the last item in the list
print stuff[-1]
# This will take off the last item of the list
print stuff.pop()

# This makes lists into a string and joins the items in the string seperated by a space
print ' '.join(stuff)
# this seperates on a # between items 3 and 5
print "#".join(stuff[3:5])

