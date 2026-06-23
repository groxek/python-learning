class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        line = s.split()
        return len(line[-1])
    

sol = Solution()
print(sol.lengthOfLastWord('Hello World'))