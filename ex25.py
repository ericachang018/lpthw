# Exercise 25: Even more practice 

def break_words(stuff): 
	"""this function will break up words for us.""" 
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""Pritns the first word after popping it off"""
	word = words.pop(0)
	print word 

def print_last_word (words):
	"""Prints the last word after popping it off"""
	word = words.pop(-1)
	print word 

def sort_sentance(sentance):
	"""Takes in a full sentance and returns the sorted words."""
	words = break_words(sentance)
	print_first_word(words)
	print_last_word(words )

def print_first_and_last(sentance):
	"""prints the first and last words of a sentance"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentance):
	"""Sorts the words then prints the first and last one"""
	words = sort_sentance(sentance)
	print_first_word(words)
	print_last_word(words)


# In the python interperter try out these commands. And play around with your functions. 
# >>> import ex25
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> wrods



