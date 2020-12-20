class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            list_s = []
            count = 0
            for si in s[i:]:
                if si in list_s:
                    ans = max(ans, count)
                    break
                else:    
                    list_s.append(si)
                    count += 1
            ans = max(ans, count)
        return ans                
