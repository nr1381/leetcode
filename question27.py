from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
            

if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    solution = Solution()
    print(solution.removeElement(nums, val)) 
