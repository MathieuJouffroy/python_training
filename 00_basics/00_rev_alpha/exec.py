import sys

len = len (sys.argv) - 1
if len < 1:
	print ("Usage: python exec.py")
while (len > 0):
	if len > 1:
		print (sys.argv[len][::-1].swapcase(), end=" ")
	else:
		print (sys.argv[len][::-1].swapcase(), end="")
	len = len - 1