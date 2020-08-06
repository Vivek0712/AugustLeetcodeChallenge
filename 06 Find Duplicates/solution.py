class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # seen = set()
        # for i in nums:
        #     if i not in seen:
        #         seen.add(i)
        # for i in seen:
        #     nums.remove(i)
        # return nums
        
        return [x for x, y in Counter(nums).items() if y> 1]