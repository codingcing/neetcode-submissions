class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we use the same trick from the palindrome question
        # for each index i, we find the subarray starting at i
        # KEY, for each index i, we just store the MAXIMUM ATTAINABLE subarray product ending at i?
        # KEY2: we ALSO need to store the MINIMUM attainable subarray ending at i

        n = len(nums)
        dp1 = [0] * n
        dp2 = [0] * n

        for i in range(n):
            if i == 0:
                dp1[i] = nums[i]
                dp2[i] = nums[i]

            else:
                dp1[i] = max(dp1[i-1] * nums[i], dp2[i-1] * nums[i], nums[i])
                dp2[i] = min(dp1[i-1] * nums[i], dp2[i-1] * nums[i], nums[i])

        return max(dp1)