class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        m=""
        while i<len(word1) or j<len(word2):
            if i<len(word1) and j<len(word2):
                m+=word1[i]+word2[j]
                i+=1
                j+=1
            elif i<len(word1):
                m+=word1[i]
                i+=1
            else:
                m+=word2[j]
                j+=1
        return m
