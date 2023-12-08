106-007
a = input()

if a[0]==a[3] and a[1]==a[2]:
	print('YES')
else:
	print('NO')
106-010
a = list(map(int, input().split() ))

N = len(a)

for i in range(1, N):
	print( a[i]*a[i], end=',' )
print()
106-012
a = list(map(int, input().split() ))

N = len(a)
ans = 0
for i in range(N-2):
	if a[i] == a[-1]:
		ans += 1

print(ans)