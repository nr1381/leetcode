from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        for n1 in range(len(nums)):
            for n2 in range(n1+1, len(nums)):
                i = n2 + 1
                j = len(nums) - 1
                while i < j:
                    if nums[n1] + nums[n2] + nums[i] + nums[j] == target:
                        if [nums[n1], nums[n2], nums[i], nums[j]] not in output:
                            output.append([nums[n1], nums[n2], nums[i], nums[j]])
                            i += 1
                            j -= 1
                        else:
                            i += 1
                            j -= 1
                    if nums[n1] + nums[n2] + nums[i] + nums[j] > target:
                        j -= 1
                    if nums[n1] + nums[n2] + nums[i] + nums[j] < target:
                        i += 1
        return output
                    
                        
        
        
            

if __name__ == '__main__':
    nums = [2,2,2,2,2]
    target = 8
    solution = Solution()
    print(solution.fourSum(nums, target)) 
