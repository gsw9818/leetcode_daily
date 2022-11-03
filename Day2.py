
from typing import List

#从左往右，从右往左分别扫描一次，求最小值
#从左往右，从右往左分别扫描一次，求最小值
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        tmp=-len(s)
        index =0
        dis_l=[0]*len(s)
        dis_r=[0]*len(s)
        dis=[0]*len(s)
        for i, Char in enumerate(s):
            if  Char == c:
                tmp = i
            dis_l [i] = i-tmp

        s=s[::-1]
        tmp=-len(s)
        for i, Char in enumerate(s):
            if  Char == c:
                tmp = i
            dis_r [i] = i-tmp

        dis_r=dis_r[::-1]
        for i in range(len(s)):
            dis[i]=min(abs(dis_l[i]),abs(dis_r[i]))
        return dis                            
solution = Solution()
solution.shortestToChar("abaa","b")
