temp_hum = [[2,6],[4,9],[12,32]]
prec_cm = [25,32,50]

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
	for i in range(len(tempHum)):
		tempHum[i][0]= tempHum[i][0]/maxTemp 
		tempHum[i][1]= tempHum[i][1]/maxHum
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
print(normOut)