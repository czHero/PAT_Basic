#答案正确
import sys

num = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
data = input()
sum = 0
for a in data:
	sum = sum+int(a)
strSum = str(sum)
flag=1
for t in strSum:
	if flag==1:
		print (num[int(t)],end='')
		flag=0
	else:
		print ('',num[int(t)],end='')