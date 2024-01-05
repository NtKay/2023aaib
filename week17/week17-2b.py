a= input()
temp=a[::-1]
for i in range(len(a)-1,-1,-1):
	print(temp[i],end='')
	if i % 3 ==0 and i != 0:
		print(',',end='')