import sys

def	operation(a, b):
        sum = a + b
        diff = a - b
        mult = a * b
        if (b != 0):
            div = a / b
            mod = a % b
        else:
            div = 'ERROR (div by zero)'
            mod = 'ERROR (modulo by zero)'
        print(f'Sum:\t\t {sum}\n'
              f'Difference:\t {diff}\n'
              f'Product:\t {mult}\n'
              f'Quotient:\t {div}\n'
              f'Remainder:\t {mod}')

argv_len = len(sys.argv) - 1
if (argv_len < 2):
	print ("Usage: python operations.py <number1> <number2>")
elif (argv_len > 2):
	print ("InputError: too many arguments")
	print ("Usage: python operations.py <number1> <number2>")
	print ("Example:\n\tpython operations.py 10 3")
else:
	try :
		operation(int(sys.argv[1]), int(sys.argv[2]))
	except ValueError:
		print ("InputError: only numbers")
		print ("Usage: python operations.py <number1> <number2>")
		print ("Example:\n\tpython operations.py 10 3")
