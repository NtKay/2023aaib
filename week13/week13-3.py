a = int(input())
if a<=2000: 
	ans = 100
else: 
	a -= 2000
	ans = 100 + a//500 *5 
	if a%500: ans += 5 
	
print(ans)

a = int(input())
if a<=2000:
	ans = 100
else:
	print( 100+(a-2000+499)//500 * 5 )