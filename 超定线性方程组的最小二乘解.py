
def Jacobi(A, b, N=500, exception=0.00001):
	'''
	A：系数矩阵
	b：增广矩阵多出来的那一列
	N：最大迭代次数
	exception：收敛系数
	'''
	k = 0
	x = [0 for i in range(len(A))]
	y = [0 for i in range(len(A))]
	sumOfLine = 0
	maxOfLine = -1
		
	while(k<N):
		for i in range(len(A)):
			sumOfLine = 0.0;
			for j in range(len(A)):
				if i != j:
					sumOfLine += A[i][j] * x[j]
					
			y[i] = (b[i] - sumOfLine) / A[i][i]
			
		maxOfLine = 0
		for i in range(len(A)):
			if maxOfLine < abs(y[i] - x[i]):
				maxOfLine = abs(y[i] - x[i])
			
		if maxOfLine > exception:
			k += 1
			for i in range(len(A)):
				x[i] = y[i]
		else:
			break
	
	print(y)
	return y
	
def mainFunc(A, b):
	
	At = []
	subAt = []
	for i in range(len(A[0])):
		for j in range(len(A)):
			subAt.append(A[j][i])
		At.append(subAt)
		subAt = []
	
	B = []
	subB = []
	
	for iAt in range(len(At)):
		for iA in range(len(A[0])):
			sumOfLine = 0
			for j in range(len(At[0])):
				sumOfLine += At[iAt][j] * A[j][iA]
			subB.append(sumOfLine)
		B.append(subB)
		subB = []
	
	#print(B)
	
	c = []
	for i in range(len(At)):
		sumOfLine = 0
		for j in range(len(At[0])):
			sumOfLine += At[i][j] * b[j]
		c.append(sumOfLine)
		
	#print(c)
	
	Jacobi(B, c,exception=0.0)
	
A = [[1,-1],[-1,2],[2,-3]]
b = [5,-4,10]
mainFunc(A, b)
#答案是19/3和1
	
	
	