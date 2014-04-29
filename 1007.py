# 答案正确 
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
			
num = int(input())
prime=getPrime(num+1)
ans=0
for i in range(1,len(prime)):
	if prime[i]-prime[i-1]==2:
		ans=ans+1
print(ans)
