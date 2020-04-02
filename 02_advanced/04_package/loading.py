import sys
import time

def progress_bar(lst):
	start_time = time.time()
	eta = 0
	bar = ">"
	progress = 5
	for x in lst:
		lst_len = len(lst)
		elapsed = time.time() - start_time
		if x != 0:
			eta = elapsed * (lst_len - (x + 1)) / (x + 1)
		perc = int(100 * (x + 1) / lst_len)
		if perc > progress:
			progress += 5
			bar = '=' + bar
		print("ETA: {:7.2f}s \033[94m[{:0>3d}%]\033[0m [\033[32m{}\033[0m] {:d}/{:d} |"
		" Elapsed time {:7.3f}".format(eta, perc, bar, x + 1, len(lst), elapsed), end='\r')
		yield x

listy = range(3333)
ret = 0
for elem in progress_bar(listy):
	ret += elem
	time.sleep(0.001)
print()
print(ret)