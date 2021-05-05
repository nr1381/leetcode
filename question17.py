from typing import List

class Solution:
    dict_phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


    def createCombinations(self, current_str, current_index, digits, output) -> List[str]:
        if current_index >= len(digits):
            if current_str != '':
                output.append(current_str)
            return output

        for data in self.dict_phone[digits[current_index]]:
            self.createCombinations(current_str+data, current_index+1, digits, output)

        return output

        
    def letterCombinations(self, digits: str) -> List[str]:
        return self.createCombinations('', 0, digits, [])
             
            

if __name__ == '__main__':
    digits = ""
    solution = Solution()
    print(solution.letterCombinations(digits)) 
