class Solution:
    def TwoSum(Self, nums: List[int], target: int) -> List[int]:
        q = {}
        for i in range(len(nums)):
            if target - nums[i] not in q:
                q[nums[i]] = i
            else:
                return ([i,q[target - nums[i]]])