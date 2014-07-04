class Song(object):
	def __init__(self,lyrics): 
		self.lyrics=lyrics 

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line 

happy_birthday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

here_is_a_new_song = ["do da",
							"this song",
							"New line",
							"best song ever!!!!"]


# yey this works! 
Song(here_is_a_new_song).sing_me_a_song()

#This works too! 
singing = Song(here_is_a_new_song)
singing.sing_me_a_song()

# here_is_a_new_song.sing_me_a_song()

# happy_birthday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()

