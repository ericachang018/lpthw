# Exercise 11 Asking Questions

# notice that we have a comma at the end of each line
# When the raw input is inserted it will stay on the same line
# as the prompt rather than print out a new line. 
print "how old are you?",
age = raw_input()
print "how tall are you?",
height = raw_input()
print "how much do you weigh",
weight = raw_input()

print "So you are %r yesrs old %r tall and %r heavy" % (age, height, weight)
