#答案正确 
import sys
n = int(input())
for i in range(n):
	datas = input()
	data = datas.split(' ')
	a = int(data[0])
	b = int(data[1])
	c = int(data[2])
	if a+b>c:
		print("Case #%d: true"%(i+1))
	else:
		print("Case #%d: false"%(i+1))