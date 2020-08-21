from random import *
from time import *
from math import *

darts = 12000000#12 million took 5.452s to finish the compute
hit = 0
#clock()
for i in range(1,darts):
	(x,y) = (random(),random())
	distant = sqrt(x**2+y**2)
	if distant <= 1.0:
		hit = hit + 1
pi = 4 * (hit/darts)
print("pi:",pi)
#print("runned for: %-5.5ss"%clock())