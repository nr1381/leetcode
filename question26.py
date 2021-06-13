from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1
            

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4,4]
    solution = Solution()
    print(solution.removeDuplicates(nums)) 
