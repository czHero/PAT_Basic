#最后个测试用例运行超时
import sys

T = int(input())
dictA = [0,0,0]#B,C,J
dictB = [0,0,0]#B,C,J
result = [0,0,0]#WIN, EQUAL, LOSE
for i in range(T):
	data = input()
	datas = data.split(' ')
	
	if datas[0]=='C':
		if datas[1]=='C':
			result[1]=result[1]+1
		elif datas[1]=='B':
			dictB[0]= dictB[0]+1
			result[2]=result[2]+1
		elif datas[1]=='J':
			dictA[1]= dictA[1]+1
			result[0]=result[0]+1
	elif datas[0]=='B':
		if datas[1]=='B':
			result[1]=result[1]+1
		elif datas[1]=='J':
			dictB[2]= dictB[2]+1
			result[2]=result[2]+1
		elif datas[1]=='C':
			dictA[0]= dictA[0]+1
			result[0]=result[0]+1
	elif datas[0]=='J':
		if datas[1]=='J':
			result[1]=result[1]+1
		elif datas[1]=='C':
			dictB[1]= dictB[1]+1
			result[2]=result[2]+1
		elif datas[1]=='B':
			dictA[2]= dictA[2]+1
			result[0]=result[0]+1
print(result[0], result[1], result[2])
print(result[2], result[1], result[0])

if dictA[0]>=dictA[1] and dictA[0]>=dictA[2]:
	print('B',end='')
elif dictA[0]<dictA[1] and dictA[1]>=dictA[2]:
	print('C',end='')
else:
	print('J',end ='')

print(' ',end='')
if dictB[0]>=dictB[1] and dictB[0]>=dictB[2]:
	print('B',end='')
elif dictB[0]<dictB[1] and dictB[1]>=dictB[2]:
	print('C',end='')
else:
	print('J',end ='')
	
	