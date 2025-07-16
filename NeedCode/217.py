#1. Brute Force
# Time & Space Complexity
#Time complexity:O(n2)
#Space complexity:O(1)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False



# 2.Hash Set
# Time & Space Complexity
#Time complexity:O(n)
#Space complexity:O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

#3. Hash Set Length
# Time & Space Complexity
#Time complexity:O(n)
#Space complexity:O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


#3. Sorting
# Time & Space Complexity
#Time complexity:O(nlogn)
#Space complexity:O(1) or O(n) depending on the sorting algorithm.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False