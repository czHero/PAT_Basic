import sys
datas = input()
data = datas.split(' ')
A = int(data[0])
B = int(data[1])
D = int(data[2])
SUM = A+B
ans = []
while SUM!=0:
	temp = SUM%D
	ans.append(temp)
	SUM = SUM//D
ans.reverse()
first = 1
if len(ans)==0:
	print('0')
else:
	for t in ans:
		if first:
			print(t,end='')
		else:
			print('',t,end='')