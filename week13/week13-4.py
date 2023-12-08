a = int(input())

a1 = a//1000 * 8 
a2 = a%1000//100 * 4
a3 = a%100//10 * 2
a4 = a%10
print( a1+a2+a3+a4)

a = input()
print( int(a[0])*8 + int(a[1])*4 + int(a[2]) *2 + int(a[3]) *1)

a = int(input(), 2)

print(a)