class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        def digit_map(digit: str):
            idx = 3 * (int(digit) - 2)
            if digit == '7':
                return alphabet[idx: idx+4]
            elif digit == '8':
                return alphabet[idx+1: idx+4]
            elif digit == '9':
                return alphabet[idx+1: idx+5]
            return alphabet[idx: idx+3]
        
        result = []
        n = len(digits)
        if n==0: return []
        def backtrack(chars, remaining):
            if len(chars) == n:
                result.append(''.join(chars[:]))
                return
            
            for i in range(len(remaining)):
                letters = digit_map(remaining[i])
                for letter in letters:
                    chars.append(letter)
                    backtrack(chars, remaining[i+1:])
                    chars.pop()
        backtrack([], digits)
        return result