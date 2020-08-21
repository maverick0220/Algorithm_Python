import cv2 as cv 
#import numpy as np
#import matplotlib.pyplot as plt
import os
import sys
import time as t

from PIL import Image

def getTimeStamp():
	
	timeStamp = str(t.localtime(t.time()))[17:-1].split(",")
	dateString = "/"
	for i in range(6):
		dateString += str(timeStamp[i].split("=")[1])
		if i > 2:
			dateString += ":"
		elif i == 2:
			dateString += "|"
		else:
			dateString += "-"
	
	path = os.getcwd()+dateString[:-1]+".txt"
	return path

def transformPictureToText(path):
	#print(path)
	image = cv.imread(path)
	
	#直接读成黑白图像
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	#gray = R * 0.299 + G * 0.587 + B * 0.114
	#print(gray)

	grayChar = ['@', '%', '8', '9', '0', '~', '/', '7', '|', '!', '1', ':', '°', '.', "'", ' ']
	#只做了16位灰度凑合用吧
	#int array[] = {127,39,46,161,58,49,33,124,55,47,126,48,54,57,56,37};的逆序
	
	fileName = getTimeStamp()
	print("saved in file: ==>",fileName)
	text = open(fileName, "x")

	#txt = []
	for i in range(len(gray)):
		line = ""
		for j in range(len(gray[0])):
			line += "{0}".format(grayChar[gray[i][j] // 16])
		#print(line)
		text.write(line+"\n")
		#txt.append(line)


	text.close()
	#for i in txt:
	#	print(i)
	
#path = sys.argv[1]#第一个值是本文件的文件名，第二个开始才是写进去的参数
#transformPictureToText(str(path))
path = os.getcwd()+'test.jps'
transformPictureToText(str(path))

'''
image = cv.imread("/Users/Maverick/Desktop/3F7693D2-631F-47B6-83A9-52894A29C0FC.png")
#cv.imshow("a",image[:,:,i])
#cv.waitKey(0)

npImage = np.array(image)
rows, cols, dimentions = image.shape

#newImage = Image.new('RGB',(2*rows,2*cols),(0,255,0))
#print("new:",newImage.size())


#直接读成黑白图像
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#print(gray)

grayChar = ['@', '%', '8', '9', '0', '~', '/', '7', '|', '!', '1', ':', '°', '.', "'", ' ']#只做了16个，凑合用吧
#int array[] = {127,39,46,161,58,49,33,124,55,47,126,48,54,57,56,37};的逆序

text = open("/Users/Maverick/Desktop/whatDoILooksLike.txt","w")

txt = []
for i in range(len(gray)):
	line = ""
	for j in range(len(gray[0])):
		line += "{0}".format(grayChar[gray[i][j] // 16])
	text.write(line+"\n")
	txt.append(line)


text.close()
for i in txt:
	print(i)

'''
#取某个通道的数值当灰度图像值
#gray = []
#for y in range(rows):
#	temp = []
#	for x in range(cols):
#		#print(image[y,x,0])
#		temp.append(image[y,x,0])
##		if x < y:
##			image[y,x,:] = [201,1,100]
#	gray.append(temp)
#	
#print(gray)
	
#plt.figure("newPic")
#plt.imshow(image)
#plt.axis('off')
#plt.show()