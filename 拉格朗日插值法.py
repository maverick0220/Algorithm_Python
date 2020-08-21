def mainFunc(x, X, Y):
	
	def baseFunc(x, a, i):
		base = 1.0
		for j in range(len(a)):
			if j != i:
				base *= (x - a[j]) / (a[i] - a[j])
		return base
		
	output = 0
	for i in range(len(Y)):
		output += Y[i] * baseFunc(x, X, i)
		
	return output
	
X = [0,1,2]
Y = [0,1,1]
x = 1.5
print(mainFunc(x, X, Y))