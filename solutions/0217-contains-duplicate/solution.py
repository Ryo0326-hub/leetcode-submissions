class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        check_set = set()
        for element in nums:
            if element not in check_set:
                check_set.add(element)
            else:
                return True
        return False

        
