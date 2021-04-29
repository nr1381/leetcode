from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0

        ans += s.count('IV') * 4
        s = s.replace('IV', '')

        ans += s.count('IX') * 9
        s = s.replace('IX', '')

        ans += s.count('XL') * 40
        s = s.replace('XL', '')

        ans += s.count('XC') * 90
        s = s.replace('XC', '')

        ans += s.count('CD') * 400
        s = s.replace('CD', '')

        ans += s.count('CM') * 900
        s = s.replace('CM', '')

        ans += s.count('I') * 1
        s = s.replace('I', '')

        ans += s.count('V') * 5
        s = s.replace('V', '')

        ans += s.count('X') * 10
        s = s.replace('X', '')

        ans += s.count('L') * 50
        s = s.replace('L', '')

        ans += s.count('C') * 100
        s = s.replace('C', '')

        ans += s.count('D') * 500
        s = s.replace('D', '')

        ans += s.count('M') * 1000
        s = s.replace('M', '')

        return ans
            

if __name__ == '__main__':
    s = 'LVIII'
    solution = Solution()
    print(solution.romanToInt(s))
