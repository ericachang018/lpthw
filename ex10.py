#Exercise 10: What was that?! 
tabby_cat = "\tI'm tabbed in."
persion_cat = "I'm spilt\non a line."
blackslash_cat ="I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persion_cat
print blackslash_cat
print fat_cat

#More Escape sequences 
#\\	Backslash ()
#\'	Single-quote (')
#\"	Double-quote (")
#\a	ASCII bell (BEL)
#\b	ASCII backspace (BS)
#\f	ASCII formfeed (FF)
#\n	ASCII linefeed (LF)
#\N{name}	Character named name in the Unicode database (Unicode only)
#\r ASCII	Carriage Return (CR)
#\t ASCII	Horizontal Tab (TAB)
#\uxxxx	Character with 16-bit hex value xxxx (Unicode only)
#\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
#\v	ASCII vertical tab (VT)
#\ooo	Character with octal value ooo
#\xhh	Character with hex value hh

#More on Escape characters in Python's Doc
#http://docs.python.org/2/reference/lexical_analysis.html
