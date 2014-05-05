import sys
data = input()
datas= data.split('E')
strnum=datas[0]
strexp=datas[1]
tmpnum=strnum.split('.');
intpart=tmpnum[0]
floatpart=''
if len(tmpnum)>1:
	floatpart=tmpnum[1]

ans=''
if int(intpart)<0:
	ans=ans+'-'
intpart=intpart[1:]
endzero=0
nodot = strnum.replace(".","")
for c in nodot:
	if c=='0':
		endzero = endzero+1
	else:
		endzero=0
if int(floatpart)==0 and int(intpart)==0:
	ans+='0'
elif int(strexp)>=len(floatpart):
	ans+=(intpart+floatpart)
	ans+=('0'* (int(strexp)-len(floatpart)))
	
elif int(strexp)>0:
	ans+=(intpart+floatpart[:int(strexp)]+'.'+floatpart[int(strexp):])

elif (-int(strexp))>=len(intpart):
	
	ans+=('0.'+'0'*(-int(strexp)-len(intpart))+intpart+floatpart)
else:
	ans+=(intpart[:int(strexp)+len(intpart)]+'.'+intpart[int(strexp)+len(intpart):]+floatpart)
i=0
for i in range(len(ans)-1):
	if (ans[i]=='0' and ans[i+1]=='.')or ans[i]!='0':
		break
print(ans[i:])	

