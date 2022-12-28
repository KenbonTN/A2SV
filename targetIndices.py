class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        print(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        return ans