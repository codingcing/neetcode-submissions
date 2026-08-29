class Solution:
    def countSubstrings(self, s: str) -> int:
        # subproblem: what is the longest palindrome STARTING at each index
        # this uses tabulation as we are ITERATING, not RECURRING

        n = len(s)
        count = 0

        for i in range(n):
            # odd palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1 
                r += 1
                l -= 1

            # even palindromes
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1 
                r += 1
                l -= 1

        return count