#答案正确
n = int(input())  
for i in range(n):
	flagp=-1  
	flagt=-1  
	isRight = True;  
	s = input()  
	for j in range(len(s)):  
		if s[j] == 'P':  
			if flagp == -1:  
				flagp = j  
			else:   
				isRight = False  
				break;  
		elif s[j] == 'T':  
			if flagt == -1:  
				flagt = j  
			else:   
				isRight = False  
				break;  
		elif s[j] != 'A':  
			isRight = False  
			break  
	if isRight == False:  
		print('NO')  
	else: 
		if flagt < flagp+2 :  
			print('NO')  
		elif len(s)-flagt-1 != (flagt-flagp-1)*flagp:  
			print('NO')  
		else:  
			print('YES')  
