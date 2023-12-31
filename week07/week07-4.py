class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n<=0: return False
        while n > 1: # 因為1是2*0不用再除了
            if n%2 != 0: #竟然餘數不是0
                return False #失敗
            n = n // 2
        # 經過樓上的檢查,都沒有出錯的話
        return True