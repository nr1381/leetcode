from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        is_break = False
        for i in reversed(range(len(nums)-1)):
            for j in reversed(range(i, len(nums))):
                if nums[i] < nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    is_break = True
                    break
            if is_break:
                nums[i+1:] = sorted(nums[i+1:])
                return nums
        nums.sort()
        return nums

if __name__ == '__main__':
    height = [4,2,0,2,3,2,0]
    solution = Solution()
    print(solution.nextPermutation(height))
