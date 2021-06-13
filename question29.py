from typing import List


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_prefix = 1
        if dividend < 0:
            dividend_prefix = -1
            dividend = int(str(dividend)[1:])

        divisor_prefix = 1
        if divisor < 0:
            divisor_prefix = -1
            divisor = int(str(divisor)[1:])
        
        sum_divisor = 0
        count = 0
        while sum_divisor <= dividend:
            shift = 0
            tmp_sum_divisor = 0
            while tmp_sum_divisor <= (dividend - sum_divisor):
                shift += 1
                tmp_sum_divisor = divisor << shift
            sum_divisor += divisor << (shift-1)
            count += (1 << (shift-1))
        count -= 1
        if count < 0:
            return 0

        if (dividend_prefix == -1 and divisor_prefix == 1) or (dividend_prefix == 1 and divisor_prefix == -1):
            count = int('-'+str(count))

        if count >= 2147483648:
            return 2147483647

        return count
            

if __name__ == '__main__':
    dividend = -2147483648
    divisor = -1
    solution = Solution()
    print(solution.divide(dividend, divisor)) 
