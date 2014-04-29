import sys
strA = input()
strlist = []
time = 1
strA="%04d"%(int(strA.replace(" ","")))

while (strA!='6174' and strA!='0000') or time!=0:
	if time!=0:
		time = time-1
	strlist.clear()
	for c in strA:
		strlist.append(c)
	strlist.sort()
	strLow=''
	for str in strlist:
		strLow+=str
	strHigh= strLow[::-1]
	numAns=int(strHigh)-int(strLow)
	strA="%04d"%(numAns)
	print (strHigh,'-',strLow,'=',strA)
