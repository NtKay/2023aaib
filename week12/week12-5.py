018
N = int(input())

for i in range(2,N+1,2):
	print(i,end=' ')
019
a = list(map(int, input().split() ))

print(min(a))
020
a = list(map(int, input().split() ))

for i in range(6):
	print(a[i]*a[i]*a[i])
18-03
n = int(input())
ans = 0
for i in range(1, n+1):
	ans += i*i
print(ans, end='')