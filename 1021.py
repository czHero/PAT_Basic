import sys
count = [0 for i in range(10)]

data = input()
for c in data:
	x = int(c)
	count[x]=count[x]+1
for i in range(len(count)):
	if(count[i]>0):
		print("%d:%d"%(i,count[i]))