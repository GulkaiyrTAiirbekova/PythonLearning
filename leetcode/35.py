class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        if target > nums[j]:
            return j + 1
        elif target < nums[i]:
            return i
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target or nums[mid-1] < target < nums[mid]:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1