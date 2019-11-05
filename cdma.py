def mult(c,d):
	return list(map(lambda x : x * d, c))

c1=[1,1,1,1]
c2=[1,-1,1,-1]
c3=[1,1,-1,-1]
c4=[1,-1,-1,1]
C=[c1,c2,c3,c4]

d=[int(x) for x in input("Enter data bits for 4 channels:").split()]
result=[]
for i in range(4):
	result.append(mult(C[i],d[i]))

print(result)
channel=[]
for i in range(4):
	res=0
	for j in range(4):
		res+=result[j][i]
	channel.append(res)

station=int(input("Enter station you want to listen:"))

res2=0
for i in range(4):
	res2+=channel[i]*C[station-1][i]

print("Data bit transmitted:",res2//4)