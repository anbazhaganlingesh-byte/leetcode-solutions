class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        let=0
        rit=len(matrix[0])-1
        top=0
        bot=len(matrix)-1
        ans=[]
        while let<=rit and top<=bot:
            for i in range(let,rit+1):
                ans.append(matrix[top][i])
            top+=1
            for i in range(top,bot+1):
                ans.append(matrix[i][rit])
            rit-=1
            if top<=bot:
                for i in range(rit,let-1,-1):
                    ans.append(matrix[bot][i])
                bot-=1
            if let<=rit:
                for i in range(bot,top-1,-1):
                    ans.append(matrix[i][let])
                let+=1
        return ans