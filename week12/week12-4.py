class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0 #迴圈前面迴圈是0
        while n>0: # 剝皮法,一次剝一層皮(第7週)
            ans += n%2 
            n = n // 2
        return ans #迴圈後面 ans拿出來用