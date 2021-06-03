import numpy as np

temp_hum = np.array([[2.0,6.0],[4.4,9.7],[12.6,32.5]])
prec_cm = np.array([25.5,32.2,50.2])

def normTempHum(tempHum):
	normVal = []
	#normalize the values
	maxTemp = 0
	maxHum = 0
	for i in tempHum:
		if i[0]>maxTemp:
			maxTemp = i[0]
		if i[1] > maxHum:
			maxHum = i[1]
	normalizer = np.array([maxTemp,maxHum])
	for i in range(len(tempHum)):
		tempHum[i][0] = tempHum[i][0]/normalizer[0]
		tempHum[i][1] = tempHum[i][1]/normalizer[1]
	return tempHum

def normPrec(prec):
	maxPrec = 0
	for i in prec:
		if i > maxPrec:
			maxPrec = i

	for i in range(len(prec)):
		prec[i] = prec[i]/maxPrec
	return prec

normIn = normTempHum(temp_hum)
print(normIn)
normOut = normPrec(prec_cm)
#print(normOut)


