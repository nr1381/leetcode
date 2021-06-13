from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        i = 0
        while i < len(haystack):
            if haystack[i:i+needle_len] == needle:
                return i
            i += 1
        return -1
            

if __name__ == '__main__':
    haystack = "aaa"
    needle = "aaaa"
    solution = Solution()
    print(solution.strStr(haystack, needle)) 
