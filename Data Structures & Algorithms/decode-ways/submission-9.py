class Solution:
    def numDecodings(self, s: str) -> int:
        # SUBPROBLEM: for each index i, we want dp[i] to be the number of decodings 
        # of the substring ENDING at index i

        # dp1 = number of ways for index i to be the FIRST number in a substring
        # dp2 = number of ways for index i to be SECOND number

        n = len(s)
        dp1 = [0] * n
        dp2 = [0] * n
        
        if s[0] == '0':
            return 0

        for i in range(n):
            if i == 0:
                dp1[i] = 1
            
            # FIRST
            if i > 0 and s[i] != '0':
                dp1[i] = dp1[i-1] + dp2[i-1] # one before it can be a first or second digit

            # SECOND
            # needs to be also less than 26
            if i > 0 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26: 
                    dp2[i] = dp1[i-1] # for one to be second, previous must be first

        return dp1[n-1] + dp2[n-1]