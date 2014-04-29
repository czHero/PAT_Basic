#答案正确 
import sys
sdata = input()
words = sdata.split(' ')
words.reverse()
first = 1
for word in words:
	if first:
		print (word,end='')
		first = 0
	else:
		print('',word,end='')