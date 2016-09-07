import random

x, y = 1.0, 1.0
n_trials = 2 ** 12
print "delta | acceptance rate"
for delta in [0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0]:
	accept = 0.0
	reject = 0.0
	for i in range(n_trials):
		del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
		if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
			x, y = x + del_x, y + del_y
			accept += 1.0
		else:
			reject += 1.0
	ar = accept / (accept + reject)
	print "%.3f \t   %f" %(delta, ar)
