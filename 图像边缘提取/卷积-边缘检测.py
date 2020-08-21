
#for t in range(32):
#	inputSize = 16
#	kernelSize = 3
#	print("changeOfKernel =",t)
#	print("inputSize   kernelSize")
#	for i in range(4):
#		print("{:4}        {:4}".format(inputSize, kernelSize))
#		inputSize = inputSize - kernelSize + 2*2 + 1
#		kernelSize += t
#	print("==============")

import numpy as np
import os

def convoluteUnit(inputs, kernel, poolSize=2, step=1):
		'''
		inputs: numpy.ndarray
		kernel: numpy.ndarray
		'''
		#padding
		#use np.zeros to create a mitrix of 0s, and put the input in it
		padding = 1
		paddedInput = np.zeros([padding * 2 + inputs.shape[0], padding * 2 + inputs.shape[0]])
		paddedInput[padding:padding+inputs.shape[0], padding:padding+inputs.shape[1]] = inputs
		#All prasie numpy!!
		
		#convolution
		convoReslut = []
		kernelSize = 3
		#kernel = np.array(kernel)
		for i in range(0,inputs.shape[0],step):
			subConvoReslut = []
			for j in range(0,inputs.shape[1],step):
				subInput = paddedInput[i:i+kernelSize, j:j+kernelSize]
				subConvoReslut.append(np.sum(subInput*kernel))
			convoReslut.append(subConvoReslut)
		
		#pooling_max
		convoReslut = np.array(convoReslut).reshape(inputs.shape)
		convoReslutShape = convoReslut.shape
		maxValues = []
		for i in range(0,convoReslut.shape[0],poolSize):
			for j in range(0,convoReslut.shape[1],poolSize):
				pool = []
				for y in range(i,i+poolSize):
					for x in range(j,j+poolSize):
						pool.append(convoReslut[y][x])
				maxValues.append(max(pool))	
		output = np.array(maxValues).reshape(round(convoReslutShape[0]/poolSize), round(convoReslutShape[1]/poolSize))
		
		#ReLU
		output[output < 0] = 0
		
		return output


kernel = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])#edge detect
import cv2 as cv
image = cv.imread(os.getcwd()+"/testPic.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

reslut = convoluteUnit(gray, kernel)

grayChar = ['@', '%', '8', '9', '0', '/', '7', '|', '!', '1', '~', ':', '°', '.', "'", ' ']
grayChar.reverse()
text = open(os.getcwd()+"/picText.txt", "w")
for i in range(1,len(reslut)):
	line = ""
	for j in reslut[i]:
		line += str(grayChar[int(j)//64])+" "
	text.write(line+"\n")
cv.imshow(reslut)
print(type(reslut))
print(reslut)


text.close()










