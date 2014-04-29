#答案正确
import sys
data = input()
datas = data.split(' ')
numB = int(datas[1])
ans = ''
res = 0
for c in datas[0]:
	numC = int(c)+res*10
	numAns = numC//numB
	ans = ans+str(numAns)
	res=numC%numB
print (int(ans), res)