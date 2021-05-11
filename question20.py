from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        data = []
        for s_elms in s:
            if s_elms == '(' or s_elms == '{' or s_elms == '[':
                data.append(s_elms)
                continue
            if len(data) == 0:
                return False
            d = data.pop(len(data)-1)
            if s_elms == ')' and d == '(':
                continue
            if s_elms == '}' and d == '{':
                continue
            if s_elms == ']' and d == '[':
                continue
            return False
        return len(data) == 0
            

if __name__ == '__main__':
    s = "{[]}"
    solution = Solution()
    print(solution.isValid(s)) 
