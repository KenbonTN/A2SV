class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsDic = {}
        ans = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    count+=1
            numsDic[nums[i]] = count
        sortedNums = []
        for k in numsDic.keys():
            sortedNums.append((k,numsDic[k]))
        sortedNums.sort()
        for s in range(len(nums)):
            x = nums[s]
            sum = 0
            for l in range(len(sortedNums)):
                if sortedNums[l][0]!=x:
                    sum+=sortedNums[l][1]
                else: 
                    break
            ans.append(sum)
        return ans
