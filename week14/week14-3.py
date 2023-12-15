106-011
a,b = list(map(int, input().split() ))

if a<b:	print(-1)
if a==b: print(0)
if a>b: print(1)

106-012
a = int(input())

if a>=90: print('A')
if 80<=a<90: print('B')
if 60<=a<80: print('C')
if a<60: print('F')

107-001
a = int(input())

a50 = a // 50
a10 = a%50 // 10
a5 = a%10 // 5 
a1 = a%5 // 1

print(f'{a}=50*{a50}+10*{a10}+5*{a5}+1*{a1}' , end='' )