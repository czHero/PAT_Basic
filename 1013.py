#全部运行超时
import sys
def getPrime(maxNum):
    aList = [x for x in range(0,maxNum)]
	
    prime = []
    for i in range(2,len(aList)):
        if aList[i] != 0:
            prime.append(aList[i])
            clear(aList[i],aList,maxNum)
    return prime
def clear(aPrime,aList,maxNum):
    for i in range(2,int((maxNum/aPrime)+1)):
        if not aPrime*i>maxNum-1:
            aList[i*aPrime]=0
			

pprime = getPrime(100000)
print(len(pprime))
datas = input()
data = datas.split(' ')
min = int(data[0])
max = int(data[1])
first = 0
for i in range(min-1,max):
	if first ==10:
		print()
		first =0
	if not first:
		print(pprime[i],end='')		
	else:
		print('',pprime[i],end='')
	first = first+1
