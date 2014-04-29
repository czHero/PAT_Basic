# 答案正确 
import sys
from operator import itemgetter
n = int(input())
list = []
ans = []

data = input()
nums = data.split(' ')
for i in range(n):
	a = int(nums[i])
	if(not list.count(a)):
		ans.append(a)
	list.append(a)
	if a%2==0:
		a=a/2
	else:
		a=(3*a+1)/2
	while a!=1:
		if(ans.count(a)>0):
			ans.remove(a)
		list.append(a)
		if a%2==0:
			a=a/2
		else:
			a=(3*a+1)/2
	
ans.sort(reverse=True)
for i in range(len(ans)):
	if i==0:
		print (ans[i],end='')
	else:
		print ('',ans[i],end='')