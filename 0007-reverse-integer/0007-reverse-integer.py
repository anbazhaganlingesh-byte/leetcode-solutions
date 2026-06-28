class Solution:
    def reverse(self, x: int) -> int:
        if -2147483648 <= x <=2147483647:
            f=True
            if x<0:
                x=x*-1
                f=False
            ans=0
            while x>0:
                d=x%10
                ans=(ans*10)+d
                x//=10
            if -2147483648 <= ans <=2147483647:
                if f:
                    return ans
                else:
                    return ans*-1
            else:
                return 0