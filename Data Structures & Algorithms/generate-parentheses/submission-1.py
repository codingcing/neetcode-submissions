class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if n == 0: return []
        def backtrack(num_open, num_close, start_index, choice):
            if num_open == num_close and len(choice) == 2*n:
                result.append(''.join(choice[:]))
                return

            if start_index == 2*n:
                return

            if num_open - num_close > 2*n - start_index or num_open < num_close:
                return
            
            for index in range(start_index, 2*n):
                choice.append('(')
                backtrack(num_open+1, num_close, index+1, choice)
                choice.pop()

                choice.append(')')
                backtrack(num_open, num_close+1, index+1, choice)
                choice.pop()

        backtrack(1, 0, 1, ['('])
        return result