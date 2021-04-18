class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output_list = [[] for i in range(numRows)]
        is_forward = True
        current_line = 1
        for i in range(len(s)):
            if current_line > numRows:
                current_line = max(1, numRows - 1)
                is_forward = False
            if current_line < 1:
                current_line = min(2, numRows)
                is_forward = True

            output_list[current_line-1].append(s[i])

            if is_forward:
                current_line += 1
            else:
                current_line -= 1

        output = ''
        for i in range(len(output_list)):
            for j in range(len(output_list[i])):
                output += output_list[i][j]

        return output


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    num = 1
    solution = Solution()
    print(solution.convert(s, num))
