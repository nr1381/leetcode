class Solution:
    def myAtoi(self, s: str) -> int:
        # step1
        step1_output = ''
        for i, s0 in enumerate(s):
            if s0 != ' ':
                step1_output = s[i:]
                break

        # step2
        step2_output = ''
        is_positive = True
        if len(step1_output) != 0 and step1_output[0] == '-':
            is_positive = False
            step2_output = step1_output[1:]
        elif len(step1_output) != 0 and step1_output[0] == '+':
            step2_output = step1_output[1:]
        else:
            step2_output = step1_output

        # step3
        step3_output = ''
        for s2 in step2_output:
            if s2.isdigit():
                step3_output += s2
            else:
                break
        if step3_output == '':
            step3_output = 0

        # step4
        step4_output = int(step3_output)

        # step5
        step5_output = step4_output
        if not is_positive:
            step5_output *= -1
        if step5_output > (2**31-1):
            step5_output = 2**31-1
        if step5_output < -2**31:
            step5_output = -2**31

        return step5_output

if __name__ == '__main__':
    x = "   +0 123"
    solution = Solution()
    print(solution.myAtoi(x))
