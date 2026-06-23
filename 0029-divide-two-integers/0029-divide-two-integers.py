class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor<0:
            if int(-1*(dividend/(divisor*-1)))>=2**31:
                return 2**31-1
            else:
                return int(-1*(dividend/(divisor*-1)))
        else:
            return int(dividend/divisor)