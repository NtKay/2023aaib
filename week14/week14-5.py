107-005
a, b = list(map(int, input().split() ))

print('Enter two numbers: The remainder is',a%b)
107-006
a, b = list(map(int, input().split() ))

if a==b: print('Enter two numbers:  It is a square ', end='')
else: print('Enter two numbers:  It is not a square ', end='')
107-007
a = input()

print(a[0],a[1],a[2],a[3],a[4],sep='   ',end='')
107-008
a = list(map(int, input().split() ))

N = len(a)

print('Enter the number of values to be processed: ',end='')

ans = 1
for i in range(1,N):
	print('Enter a value: ',end='')
	ans *= a[i]
	
print('Product of the',a[0],'values is',ans,end='')