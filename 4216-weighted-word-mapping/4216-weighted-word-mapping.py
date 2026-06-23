class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        m=""
        for i in words:
            n=0
            for j in i:
                n+=weights[(ord(j)-97)]
            n=n%26
            m+=chr(122-n)
        return m           