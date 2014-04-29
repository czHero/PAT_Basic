#答案正确
import sys

num = int(input())

hun = num//100
for i in range(hun):
	print('B',end='')
num = num%100
decmical = num//10
for i in range(decmical):
	print('S',end='')
left =num%10
for i in range(left):
	print(i+1,end='')
	
