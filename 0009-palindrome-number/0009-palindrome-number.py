class Solution:
    def isPalindrome(self, x: int) -> bool:
        m=str(x)
        if m==m[::-1]:
            f=bool(1)
        else:
            f=bool(0)
        return f
            
        