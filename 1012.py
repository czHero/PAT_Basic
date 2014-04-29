#答案正确
import sys

datas = input()
data = datas.split(' ')
A1 = 0
A2 = 0
numA2 = 0
flagA2 = 1
A3 = 0
A4 = 0.0
numA4=0
A5 = 0
for i in range(1,len(data)):
	num = int(data[i])
	if num%5==0:
		if num%2==0:
			A1=A1+num
	elif num%5==1:
		numA2=numA2+1
		if flagA2:
			A2=A2+num
			flagA2=0
		else:
			A2=A2-num
			flagA2=1
	elif num%5==2:
		A3=A3+1
	elif num%5==3:
		A4=A4+num
		numA4=numA4+1
	else:
		if A5<num:
			A5=num
if A1==0:
	print('N',end='')
else:
	print(A1,end='')
if numA2==0:
	print('','N',end='')
else:
	print('',A2,end='')
if A3==0:
	print('','N',end='')
else:
	print('',A3,end='')
if numA4==0:
	print('','N',end='')
else:
	print('','%.1f'%(A4/numA4),end='')
if A5==0:
	print('','N',end='')
else:
	print('',A5,end='')
	
	
	
	
		