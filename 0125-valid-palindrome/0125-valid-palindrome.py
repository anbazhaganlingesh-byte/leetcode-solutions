class Solution:
    def isPalindrome(self, s: str) -> bool:
        m=""
        for i in s:
            if i.isalpha() or i.isdigit():
                m+=i
        m=m.lower()
        if m==m[::-1]:
            return True
        else:
            return False