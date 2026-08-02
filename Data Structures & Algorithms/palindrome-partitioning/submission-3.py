class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)  
        result = []

        def isPalindrome(string):
            m = len(string)
            for i in range(m):
                if string[i] != string[m-1-i]:
                    return False
            return True
    
        def backtrack(unused, chars):
            if chars:
                if not bool(chars[-1]) or not isPalindrome(chars[-1]):
                    return

            if len(''.join(chars)) == n:
                result.append(chars[:])
                return

            for index in range(len(unused)):
                chars.append(unused[:index+1])
                backtrack(unused[index+1:], chars)
                chars.pop()

        backtrack(s, [])
        return result