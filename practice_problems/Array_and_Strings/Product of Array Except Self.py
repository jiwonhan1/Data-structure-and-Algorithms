class Solution(object):
    # Let and right product lists
    # Time complexity O(N)
    # Space complexity O(N)
    def productExceptSelf(self, nums):
        # The length of the input array
        length = len(nums)
        # The left and right arrays
        L, R, answer = [0] * length, [0] * length, [0] * length
        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no element to the left,
        # so the L[0] would be 1
        L[0] = 1

        for i in range(1, length):

            # L[i-1] already contains the product of elements to the left of 'i-1'
            # Simply multiplying it with nums[i-1] would give the producf of all elements to the left of index 'i'
            L[i] = nums[i-1] * L[i-1]

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length -1', there are no elements to the right,
        # so the R[length-1] would be 1
        R[length -1] = 1

        for i in reversed(range(length -1)):
            # R[i+1] already contains the product of elements to the right of 'i+1'

            # Simply multiplying it with nums[i+1] would give the product of all elements to the right of index 'i'
            R[i] = R[i + 1] * nums[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except shelf
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]
        return answer

    # O(1) space approach
    def productExceptSelf(self, nums):
        length = len(nums)

        answer = [0] * length

        answer[0] = 1

        for i in range(1, length):
            answer[i] = nums[i-1] * answer[i-1]

        R = 1

        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer