### 思路

对每一位分别加减，

### 代码


```python3

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        res=[]
        i=len(num)-1
        s=0
        carry=0
        while i>=0 or k!=0:
            x=num[i] if i>=0 else 0
            y=k % 10
            s = x + y + carry
            carry =s // 10
            k //= 10

            i -= 1
            res.insert(0,s%10)
        
        if carry != 0:
            res.insert(0,carry)
        return res

```

**复杂度分析**
- 时间复杂度：O(N)，
- 空间复杂度：O(N)
