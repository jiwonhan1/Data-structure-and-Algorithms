class Solution(object):
    # Time complexity O(N)
    # Space complexity O(N)
    def productExceptSelf(self, nums):
        length = len(nums)

        L, R, answer = [0] * length, [0] * length, [0] * length

        L[0] = 1

        for i in range(1, length):
            L[i] = nums[i-1] * L[i-1]

        R[length -1] = 1

        for i in reversed(range(length -1)):
            R[i] = R[i + 1] * nums[i + 1]

        for i in range(length):
            answer[i] = L[i] * R[i]
        return answer