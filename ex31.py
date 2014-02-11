print "you enter a dark room with two doors. do you go though door number 1 or door number 2?"

door = raw_input("> ")

if door == "1":
    print "there's a ginat bear here ating cheese cake what do you do?"
    print "1. take the cake"
    print "2. scream at the bear?"

    bear = raw_input("> ")
    if bear == "1":
        print "bear eats your face off good job!"
    elif bear == "2":
        print "bear eats your legs off good job!"
    else:
        print "well, doing %s is probably better. Bear runs away" % bear

elif door == "2":
    print "you stare into the endless abyss at the cthulh's retina"
    print "1. blueberries"
    print "2. yellow jacket clothpins "
    print "3. understanding revoles yelling melodies"

    insantiy = raw_input("> ")

    if insanity == "1" or   insanit == "2":
        print "your body survieds powered by a mid of jelly good job"
    else:
        print "the insanity rots your eyes into a pull of puck good job"
else:
    print "you stumble and fall on a knife and die good job!"
