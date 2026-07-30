class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def backtrack(choice, remaining):
            if len(choice) == n:
                result.append(choice[:])
                return

            for idx in range(len(remaining)):
                choice.append(remaining[idx])
                backtrack(choice, remaining[:idx]+remaining[idx+1:])
                choice.pop()

        backtrack([], nums)
        return result