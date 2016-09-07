import random, math

n_trials = 400000
mean_sum = 0.0
mean_sum_square = 0.0
n_hits = 0

for iter in range(n_trials):
	x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
	Obs = 0.0
	if x**2 + y**2 < 1.0: 
		n_hits += 1
		Obs = 4.0
	mean_sum += Obs
	mean_sum_square += Obs**2

mean = mean_sum/n_trials
mean_squared = mean_sum_square/n_trials
print "Mean: %f" % (mean)	
print "Mean Squared: %f" %(mean**2)
print "Mean of Squares: %f" % (mean_squared)
print "Variance: %f" % (mean_squared - mean ** 2)
print "Standard Deviation: %f" % (math.sqrt(mean_squared - mean ** 2))

