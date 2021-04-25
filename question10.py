class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        while True:
            if i >= len(s) and j >= len(p):
                return True
            if i >= len(s) and j < len(p):
                if p[j] == '*' or p[j] == '.':
                    j += 1
                    continue
                return False
            if j >= len(p):
                return False

            if s[i] == p[j]:
                i += 1
                j += 1
                continue

            if p[j] == '.':
                i += 1
                j += 1
                continue

            if p[j] == '*':
               if s[i] == p[j-1] or p[j-1] == '.':
                   i += 1
                   continue
               else:
                   j += 1
                   continue

            if s[i] != p[j]:
                if (j + 1) < len(p) and p[j+1] == '*':
                    j += 2
                    continue

            return False

if __name__ == '__main__':
    s = "ab"
    p = ".*c"
    solution = Solution()
    print(solution.isMatch(s, p))                 
