class Solution:
    def reverse(self, x: int) -> int:
        num = 1
        if x < 0:
            num = -1
            x = abs(x)
        ans = int(str(x)[::-1]) * num
        if ans < (-2**31) or ans > (2**31 - 1):
            ans = 0
        return ans

if __name__ == '__main__':
    x = -123
    solution = Solution()
    print(solution.reverse(x))
