class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m=0
        for i in digits:
            m=(m*10)+i
        m+=1
        m=[int(ch) for ch in str(m)]
        return m