class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mi=6.0*minutes
        ho=30.0*(hour%12)+0.5*minutes
        d=abs(ho-mi)
        return min(d,360.0-d)