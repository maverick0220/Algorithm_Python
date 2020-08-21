import random as r
'''
<README>
#this function is made to divide a group of vectors by k-mean
#could support vectors as high as you want, but to display it out, vector should only has 2 dimensions(could be 3 dimensions, but I'm too lazy to edit the code anymore becuase I wanna play games....
</README>
'''

def k_MeanClassifer(typeNumber, data):
	'''
	typeNumber:how many groups are you going to divid
	data: a list that full of things to sort
	data element:should also be a list,contains demension distance
	'''
	
	vectorWidth = len(data[0])
	dataLength = len(data)
	centers = []
	typeMarker = [0 for i in range(dataLength)]
		
	def sortThingsByCenters(centers):
		for i in range(dataLength):
				if typeMarker[i] != -1:
					minDistance = 1000000000
					distance = 0
					
					for c in centers:
						for v in range(vectorWidth):
							#print("c:",c)
							if isinstance(c, int):
								distance += (data[i][v] - data[c][v])**2#欧氏距离
							else:
								distance += (data[i][v] - c[v])**2
						distance = distance ** 0.5
						
						if distance < minDistance:
							minDistance = distance
							typeMarker[i] = c
		return typeMarker
	
	#step1: randomly find n dot as start
	while(True):
		centers = [r.randint(0,dataLength-1) for i in range(typeNumber)]
		if len(set(centers)) == typeNumber:
			break
	print("first centers:",centers)
	
	for i in centers:
		#print("-i:",i)
		typeMarker[i-1] = i - 1
		
	
	#step2: frist divide
	typeMarker = sortThingsByCenters(centers)
	print("typeMarker:", typeMarker)
	
	#step3: do the loop thing till no other changes happen in the divided groups
	while (True):
		newCenters = []
		for marker in set(typeMarker):
			newCenter = [0 for i in range(vectorWidth)]
			counter = 0
			for v in range(dataLength):
				if marker == typeMarker[v]:
					counter += 1
					for i in range(vectorWidth):
						newCenter[i] += data[v][i]
			if counter > 0:
				newCenters.append(list(map(lambda x: x / counter, newCenter)))
			
		print(list(newCenters))
		newMarker = sortThingsByCenters(newCenters)
		if newMarker == typeMarker:
			typeMarker = newMarker
			break
		else:
			typeMarker = newMarker
	
	#step4: ready to output....data structre takes most of my time( ´Д`)y━･~~
	sortedData = [[] for i in range(typeNumber)]
	index = []
	for i in typeMarker:
		if i not in index:
			index.append(i)
		
	for i in range(dataLength):
		for j in range(typeNumber):
			if typeMarker[i] == index[j]:
				sortedData[j].append(data[i])
				break

	return (sortedData, newCenters)
		
	
data = [[r.randint(0,9),r.randint(0,9)] for i in range(20)]
print(data)

reslut, centers = k_MeanClassifer(2,data)
print("reslut:")
for i in range(len(reslut)):
	print("group_"+str(i)+":", reslut[i])


#show the data out....if the data has dimensions higher than 3, it would be very hard to show
#as data were divided in 2 groups, they'll have blue and red to indicate which group they're in. And the hollow cricles among colored dots are the centers of their belonging groups.(also becuase of some ass-pain bugs I haven't frigure out yet and I wouldn't want to, the color of circles might be on contrary....)
import matplotlib.pyplot as plt

group_1_x = [i[1] for i in reslut[0]]
group_1_y = [i[0] for i in reslut[0]]

group_2_x = [i[1] for i in reslut[1]]
group_2_y = [i[0] for i in reslut[1]]

plt.scatter(group_1_x, group_1_y, s=200, label = '$Group_1$', c = 'blue', marker='.', alpha = None, edgecolors= 'white')
plt.scatter(centers[0][1], centers[0][0], s=200, label = '$Group_1_center$', c = 'white', marker='.', alpha = None, edgecolors= 'blue')
#in `label`, use '$ $' to express LaTex formula, here is just for fun

plt.scatter(group_2_x, group_2_y, s=200, label = '$Group_2$', c = 'red', marker='.', alpha = None, edgecolors= 'white')
plt.scatter(centers[1][1], centers[1][0], s=200, label = '$Group_2_center$', c = 'white', marker='.', alpha = None, edgecolors= 'red')

plt.show()


