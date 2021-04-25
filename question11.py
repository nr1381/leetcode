from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = 0
        while i != j:
            if height[i] >= height[j]:
                ans = max(height[j]*(j-i), ans)
                j -= 1
            else:
                ans = max(height[i]*(j-i), ans)
                i += 1
            print(f'i:{i} j:{j} ans:{ans}')
        return ans

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(height))
