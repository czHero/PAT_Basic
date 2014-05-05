#第五个测试点超时
import sys
class node:
	addr=0
	value=0
	next=0
	def __init__(self,addr,value,next):
		self.addr=addr
		self.value=value
		self.next=next

data=input()
datas = data.split(' ')
value = []
for j in range(len(datas)):
	if datas[j].isdecimal():
		value.append(datas[j])

init_addr=int(value[0])
N = int(value[1])
K = int(value[2])
nodes = {}
for i in range(N):
	data=input()
	datas = data.split(' ')
	tvalue = []
	for j in range(len(datas)):
		if datas[j].isdecimal() or datas[j]=='-1':
			tvalue.append(datas[j])
	
	nodes[int(tvalue[0])]= node(int(tvalue[0]),int(tvalue[1]),int(tvalue[2]))
	
index = init_addr
listnode =[] 
while index!=-1:
	listnode.append(nodes[index])
	index = nodes[index].next
	
result =[]
index=0
while index+K<=len(listnode):
	tmplist = listnode[index:index+K]
	tmplist.reverse()
	result+=tmplist
	index = index+K
result += listnode[index:len(listnode)]
if len(result)>1:	
	for i in range(len(result)-1):
		result[i].next=result[i+1].addr
		print("%05d %d %05d"%(result[i].addr,result[i].value,result[i].next))
	print("%05d %d -1"%(result[i+1].addr,result[i+1].value))
else:	#若只有一条输入
	print("%05d %d -1"%(result[0].addr,result[0].value))


