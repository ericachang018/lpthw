# Exercise 35 Branches and Functions

from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	next = raw_input("> ")
	if "0" in next or "1" in next: 
		how_much=int(next)
	else: 
		dead("Man learn to type a Number.")
	
	if how_much < 50: 
		print "Nice, you're not greedy, You win!"
		exit(0)
	else:
		dead("you greedy bastard!")

def bear_room():
	print "There's a bear in here."
	print "The bear has a bunch of honey"
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")
		if next == "take honey":
			dead("The bear looks at you then slaps your face off")
		elif next == "taunt bear" and not bear_moved:
			print "the bear has moved fromt he door. You can go to through it now"
			bear_moved = True 
		elif next == "taunt bear" and bear_moved: 
			dead("bear gets pissed off and chews off your leg")
		elif next == "open door" and bear_moved: 
			gold_room()
		else:
			print "I have no idea what that means"

def ctulhu_room():
	print "here you see the great evil cthulhu"
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	next = raw_input("> ")

	if "flee" in next: 
		start()
	elif "head" in next: 
		dead("well that was tast!")
	else:
		ctulhu_room()

def dead(why):
	print why, "good job!"
	exit(0)

def start():
	print "you are in a dark room."
	print "there is a door to your right and left"
	print "which one do you take?"

	next = raw_input("> ")
	if next == "left": 
		bear_room()
	elif next == "right":
		ctulhu_room()
	else:
		dead("you stumble around the room till you starve and die")

start()

	
