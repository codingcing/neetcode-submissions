class Solution:
    def rob(self, nums: List[int]) -> int:
        # maxes has index i storing the MAXIMUM robbable STARTING clockwise from 1
        # this wont work in general since we dont include the wraparound
        # so we also do the maxium going ANTICLOCKWISE from n-1
        # need to account for the fact that 0 and n-1 are ADJACENT

        n = len(nums)
        maxes_fwd = [0] * n
        maxes_bwd = [0] * n

        for i in range(n):
            if i==0:
                maxes_fwd[i] = nums[i]
                maxes_bwd[i] = nums[n-1-i]
            
            elif i == 1:
                maxes_fwd[i] = max(nums[i], maxes_fwd[i-1])
                maxes_bwd[i] = max(nums[n-1-i], maxes_bwd[i-1])

            elif i == n-1:
                maxes_fwd[i] = maxes_fwd[i-1]
                maxes_bwd[i] = maxes_bwd[i-1]

            else: 
                maxes_fwd[i] = max(nums[i] + maxes_fwd[i-2], maxes_fwd[i-1])
                maxes_bwd[i] = max(nums[n-1-i] + maxes_bwd[i-2], maxes_bwd[i-1])

        return max(max(maxes_fwd), max(maxes_bwd))

