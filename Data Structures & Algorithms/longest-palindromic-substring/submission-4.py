class Solution:
    def longestPalindrome(self, s: str) -> str:
        # SUBPROBLEM: what is the longest palindrome which is CENTERED at index i, for each index
        # we need to catch both ODD and EVEN length palindromes

        n = len(s)
        maxLen, maxWord = 0, ""

        for i in range(n):
            # odd length
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    maxWord = s[l:r+1]
                r+=1
                l-=1

            # even length
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    maxWord = s[l:r+1]
                r+=1
                l-=1
        
        return maxWord