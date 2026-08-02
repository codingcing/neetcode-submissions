class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def subset_recur(idx, subset):
            if subset not in result:
                result.append(subset[:])
            
            if idx == len(nums):
                return
            
            subset_recur(idx+1, subset + [nums[idx]])
            subset_recur(idx+1, subset)

        subset_recur(0, [])
        return result