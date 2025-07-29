class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maxarea=0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         w=height[j]-height[i]
        #         n=min(height[i], height[j])
        #         area=n*w
        #         maxarea=max(maxarea, area)

        # return maxarea
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            diff = right - left
            Lheight = height[left]
            Rheight = height[right]
            mindiff = min(Lheight, Rheight)
            area2 = diff * mindiff
            area = max(area, area2)
            if Lheight <= Rheight:
                left += 1
            else:
                right -= 1
        return area

