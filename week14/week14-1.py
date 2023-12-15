class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notAns = set()

        for a,b in paths: #先巡第一次
            notAns.add(a) #出發點不是答案

        for a,b in paths: #第二輪
            if b not in notAns: #b不再出發裡,就是答案
                return b #B 不是答案