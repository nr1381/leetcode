from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num12 = nums1 + nums2
        num12.sort()
        size12 = len(num12)
        print(num12)

        ans = 0
        if size12 % 2 == 0:
            d_size12 = int(size12 / 2)
            ans = (num12[d_size12 - 1] + num12[d_size12]) / 2
        else:
            d_size12 = int(size12 / 2)
            ans = num12[d_size12]

        return ans

if __name__ == '__main__':
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    solution = Solution()
    print(solution.findMedianSortedArrays(num1, num2))        
