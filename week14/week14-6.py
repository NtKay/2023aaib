107-009
a = int(input())

if a-2 > 0:
	print( a - 2, end='')
else:
	print( 2 - a, end='')
107-010
a = int(input())

ans = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
print(ans[a],end='')
107-010
a = int(input())
if a==2: print(28)
elif a==4 or a==6 or a==9 or a==11: print(30, end='')
else: print(31, end='')