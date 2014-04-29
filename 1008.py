#答案正确 
import sys
sdata = input()
data = sdata.split(' ')
n = int(data[0])
m = int(data[1])
m = m%n
sdata = input()
data = sdata.split(' ')
first = 1
for i in range(n-m, n):
	if first:
		print (data[i],end='')
		first = 0
	else:
		print ('',data[i],end='')
for i in range(n-m):
	if first:
		print (data[i],end='')
		first = 0
	else:
		print ('',data[i],end='')

