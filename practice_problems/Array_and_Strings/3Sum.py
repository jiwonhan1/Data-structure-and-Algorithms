class Solution(object):
    # Time complexity O(n2)
    # Sorting the array would not change the overall time comlexity
    # Space complexity O(N)
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums,i,res)
        return res
    def twoSum(self, nums, i, res):
        lo, hi = i +1, len(nums) -1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and lo[i-1] == lo[i]:
                    lo += 1

    def threeSum2(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum2(nums, i, res)
        return res
    def twoSum2(self, nums, i, res):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j+1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
            seen.add(j)
            j += 1