import sys

argv_len = len (sys.argv) - 1
if (argv_len) < 1 or (argv_len) > 1:
	print ("Usage: python whois.py")
else:
	try:
		x = int(sys.argv[1])
		if (x == 0):
			print ("I'm Zero.")
		elif (x % 2 == 0):
			print ("I'm Even.")
		else:
			print ("I'm Odd.")
	except ValueError:
		print ("ERROR")