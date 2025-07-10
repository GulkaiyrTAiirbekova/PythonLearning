# candies = [5,2,3,1,7,6]
# for i in candies:
#     print('i: ', i)

class Solution:
    # A list candies where each element represents the number of candies a child has.
    # An integer extraCandies which you can give to any one child.
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies) #find current max([2,5,6,7,1])->7
        # So the goal is: can a child’s total (candies + extra) be ≥ 7?
        return [c + extraCandies >= max_candy for c in candies]
candies = [2,5,6,7,1]
extraCandies =3

max_candy =7 # current max
