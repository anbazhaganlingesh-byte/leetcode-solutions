class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m=s=0
        for i in range(len(gain)):
            s+=gain[i]
            m=max(m,s)
        return m