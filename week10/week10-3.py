a =list(map(int ,input().split() ))

if a[0]>=a[1] and a[0]>=a[2]: ans=a[0]
if a[1]>=a[0] and a[1]>=a[2]: ans=a[1]
if a[2]>=a[0] and a[2]>=a[1]: ans=a[2]
#ans = max(a)

print( ans )

a = list(map(int, input().split() ))

ans = sum(a) - a[0]

print(ans)

