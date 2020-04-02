t = ( 0, 4, 132.42222, 10000, 12345.67)
print("day_{:0>2d}".format(t[0]),\
 "ex_{:0>2d} : {:3.2f}".format(t[1], t[2]),\
 "{:.2e}".format(t[3]), "{:.2e}".format(t[4]), sep=", ")
