from string import printable
print(printable[62:])

class Solution:
    def isPalindrome(self, s: str) -> bool:
        for x in printable[62:]:
            s = s.replace(x, '')
        return s.lower() == s[::-1].lower()
    

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sclean = ''.join(x.lower() for x in s if x.isalnum())
        return sclean == sclean[::-1]
    

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))