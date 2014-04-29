import sys

class item:
	def __init__(self,num,price):
		self.num=num
		self.price = price
		self.pprice = price/num
	def Pprice(self):
		return self.pprice
MoonCake = [] 
ans = 0.0
data = input()
datas = data.split(' ')
N = int(datas[0])
D = int(datas[1])
data = input()
dataNUM = data.split(' ')
data = input()
dataPRICE = data.split(' ')

for i in range(N):
	a = item(float(dataNUM[i]),float(dataPRICE[i]))
	MoonCake.append(a)
MoonCake.sort(key=item.Pprice, reverse = True)
for i in range(N):
	if MoonCake[i].num<D:
		ans +=MoonCake[i].price
		D-=MoonCake[i].num
	else:
		ans+=MoonCake[i].pprice*D
		break
print("%.2f"%(ans))