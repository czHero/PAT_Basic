import sys
datas = input()
data = datas.split(' ')
num = []
for i in range(len(data)):
	for j in range(int(data[i])):
		num.append(i)


index =0
for i in range(len(num)):
	if int(num[i])!=0:
		print(num[i],end='')
		index =i
		break
for i in range(len(num)):
	if i !=index:
		print(num[i],end='')