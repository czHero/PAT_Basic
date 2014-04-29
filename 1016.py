#答案正确
import sys
data = input()
datas = data.split(' ');
strA = ''
strB = ''
for c in datas[0]:
	if c == datas[1]:
		strA=strA+c
		
for c in datas[2]:
	if c == datas[3]:
		strB=strB+c
if strA=='':
	numA = 0
else:
	numA = int(strA)
if strB=='':
	numB=0
else:
	numB = int(strB)
print(numA+numB)