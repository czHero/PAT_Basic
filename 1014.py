#答案正确
import sys
Day = {'A':'MON', 'B':'TUE', 'C':'WED','D':'THU','E':'FRI','F':'SAT','G':'SUN'}
HH = {'0':'00','1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09',
'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15','G':'16','H':'17',
'I':'18','J':'19','K':'20','L':'21','M':'22','N':'23'
}
day = ''
hh = ''
mm = ''
strA = input()
strB = input()
lenA = len(strA)
lenB = len(strB)
for i in range(lenB if lenA>lenB else lenA):
	if strA[i]==strB[i] and strA[i]==strA[i].upper() and strA[i].isalpha():
		try:
			day = Day[strA[i]]
			break
		except:
			continue
for j in range(i+1, lenB if lenA>lenB else lenA):
	if strA[j]==strB[j]:		
		try:
			hh = HH[strA[j]]
			break
		except:
			continue
strA = input()
strB = input()
lenA = len(strA)
lenB = len(strB)
for i in range(0, lenB if lenA>lenB else lenA):
	if strA[i]==strB[i] and strA[i].isalpha():
		mm = '%02d'%i
		break
print(day,"%s:%s"%(hh,mm))