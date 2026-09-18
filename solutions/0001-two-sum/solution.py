class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        check_dict = {}
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in check_dict:
                return [i, check_dict[complement]]
            else:
                check_dict[num] = i


        
