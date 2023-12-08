106-003
a = list(map(int, input().split() ))
N =len(a)-1
for i in range(N-1, -1, -1):
	print( a[i], end=' ')
print()
106-009
a = input()
N = len(a)
for i in range(N-1, -1, -1):
	print(a[i], end='')
print()

a = int(input())
while a>0:
	print(a%10,end='')
	a = a // 10
print()