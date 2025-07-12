class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # Greedy Approach 1.
        longest, curr_length = 0, 0

        for num in nums:
            if num <= threshold and curr_length % 2 == num % 2:
                curr_length += 1
            else:
                longest = max(longest, curr_length)

                if num > threshold or num % 2 == 1:
                    curr_length = 0
                else:
                    curr_length = 1

        return max(curr_length, longest)

        # O(n) time.
        # O(1) space.

    def longestAlternatingSubarray2(self, nums, threshold):
        # Greedy Approach 2.
        longest, current_length = 0, 0

        for i in range(len(nums)):

            if nums[i] <= threshold:
                if current_length == 0 and nums[i] % 2 == 0:
                    current_length = 1
                elif current_length > 0 and nums[i] % 2 != nums[i - 1] % 2:
                    current_length += 1
                else:
                    if nums[i] % 2 == 0:
                        current_length = 1
                    else:
                        current_length = 0
            else:
                current_length = 0

            longest = max(longest, current_length)

        return longest

        # O(n) time.
        # O(1) space.

    def longestAlternatingSubarray3(self, nums: List[int], threshold: int) -> int:
        # Sliding Window.
        longest = 0

        for left in range(len(nums)):
            if nums[left] % 2 == 0 and nums[left] <= threshold:

                right = left
                while (
                        right < len(nums) - 1 and
                        nums[right] % 2 != nums[right + 1] % 2 and
                        nums[right + 1] <= threshold
                ):
                    right += 1

                longest = max(longest, right - left + 1)
        return longest

        # O(n * n/2) -> O(n^2) time.
        # O(1) space.