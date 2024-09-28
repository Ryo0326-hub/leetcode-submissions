class Solution:
    def numberOfSteps(self, num: int) -> int:
        Count = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
                Count+=1
            else:
                num-=1
                Count+=1
        return Count
        
