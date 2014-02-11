# Exercise 30 if's and elifs
people = 30
cars = 40
buses = 15
if cars > people:
    print "we shouldd take cars"
elif cars < people:
    print "we should not take cars"
else:
    print "We can't decide"

if buses > cars:
    print "thats too many buses"
elif buses < cars:
    print "maybe we should take the bus"
else:
    print "we still can't decide"

if people > buses:
    print "alright, lets just take the buses"
else:
    print "fine lets jus stay home"
