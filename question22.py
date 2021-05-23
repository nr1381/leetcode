from typing import List


class Solution:
    def createBrackets(self, n, i, j, current, output):
        if i == n and j == n:
            output.append(current)
            return output

        if i == n:
            return self.createBrackets(n, i, j+1, current+')', output)

        if j == n or i <= j:
            return self.createBrackets(n, i+1, j, current+'(', output)

        self.createBrackets(n, i+1, j, current+'(', output)
        self.createBrackets(n, i, j+1, current+')', output)

        return output
        

    def generateParenthesis(self, n: int) -> List[str]:
        return self.createBrackets(n, 0, 0, '', [])

if __name__ == '__main__':
    n = 8
    solution = Solution()
    print(solution.generateParenthesis(n)) 
