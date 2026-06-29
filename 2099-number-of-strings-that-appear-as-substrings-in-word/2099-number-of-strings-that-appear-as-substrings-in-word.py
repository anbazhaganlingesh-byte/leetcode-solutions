class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        co=0
        for i in patterns:
            if i in word:
                co+=1
        return co