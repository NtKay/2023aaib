s = [1,2,3,4] #第一種用大括號
print(s)
s = set( (1,3,5,7) )
print(s)
s = set( [1,2,4,3] )#第二種的set() 裡面也可以放[方括號]list陣列的東西 
print(s)
s = set('Hello') #第二種的set() 裡面也可以放字串 會把他一個個拆解
print(s)

s.add(100)
print(s)
s.remove('H')
print(s)