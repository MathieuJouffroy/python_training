import sys
import string

def text_analyser(text=""):	
	count_upper = 0
	count_lower = 0
	count_space = 0
	count_marks = 0
	if not text:
		text_analyser(input ("What is the text to analyse?\n"))
	else:
		for letter in text:
			if letter.isupper():
				count_upper += 1
			if letter.islower():
				count_lower += 1
			if letter.isspace():
				count_space += 1
			if letter in string.punctuation:
				count_marks += 1
		print ("The text contains {} characters:"\
		.format(count_marks + count_upper + count_lower + count_space))
		print ("- {0} upper letters\n- {1} lower letters\n- {2} spaces\n- {3} punctuation marks"\
		.format(count_upper, count_lower, count_space, count_marks))

argv_len = len (sys.argv) - 1
if argv_len != 1:
	text_analyser()
else:
	text_analyser(sys.argv[1])
