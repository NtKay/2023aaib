107-002
a = int(input())

if a<=1500:	ans = 100
else:
	ans = 100 + (a-1500) // 250 * 5
	if ((a-1500) % 250) > 0:
		ans += 5
	
print(ans, end='')
107-002
a = int(input())

if a<=1500: ans = 100
else: ans = 100 + (a-1500+249) // 250 * 5

print(ans , end='')
107-003
a ,b = list(map(int, input().split() ))
print(a%b, end='')