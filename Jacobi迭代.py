	
def Jacobi(A, b, N=500, exception=0.00001):
	
#A:系数矩阵
#b:增广矩阵多出来的那一列
#N:最大迭代次数
#exception:收敛系数

	k = 0
	x = [0,0,0]
	y = [0,0,0]
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
	

A = [[10, -1, -2], [-1,10,-2], [-1,-1,5]]
b = [72, 83, 42]

Jacobi(A, b,70,0)
