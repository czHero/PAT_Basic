#答案正确
import sys
x=[]
exp=[]
data = input()
datas = data.split(' ')
t=0
for i in range(len(datas)):
	if t%2==0:
		try:
			tmp = int(datas[i])
			x.append(tmp)
			t=t+1
		except:
			pass
		
	else:
		try:
			tmp = int(datas[i])
			exp.append(tmp)
			t=t+1
		except:
			pass
		
first=1
for i in range(len(x)):
	if exp[i]!=0 and x[i]!=0:
		if first:
			print(exp[i]*x[i], exp[i]-1,end='')
			first=0
		else:
			print('',exp[i]*x[i], exp[i]-1,end='')
		
if first:
	print('0 0')