#答案正确
import sys

maxName =''
maxID = ''
maxSorce = -1
minName =''
minID =''
minSorce = 101
n = int(input())
for i in range(n):
	data = input()
	texts = data.split(' ')
	if int(texts[2])>maxSorce:
		maxSorce = int(texts[2])
		maxName = texts[0]
		maxID = texts[1]
	if int(texts[2])<minSorce:
		minSorce = int(texts[2])
		minName = texts[0]
		minID = texts[1]
print (maxName,maxID)
print (minName,minID)