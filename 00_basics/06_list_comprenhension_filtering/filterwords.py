import sys

def 	filter_words(string, nb):
	word_list = string.split()
	return ([word for word in word_list if len(word) > nb])

argv_len = len (sys.argv) - 1
if (argv_len < 2 or argv_len > 2):
	print ("ERROR Usage: python filterwords.py <string> <n_letters>")
else:
	try:
		print (filter_words(sys.argv[1], int(sys.argv[2])))
	except ValueError:
		print ("ERROR")
