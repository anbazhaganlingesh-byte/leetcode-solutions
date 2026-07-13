class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        c=1
        arr=[[0]*n for _ in range(n)]
        let=0
        rit=n-1
        top=0
        bot=n-1
        while let<=rit and top<=bot:
            for i in range(let,rit+1):
                arr[top][i]=c
                c+=1
            top+=1
            for i in range(top,bot+1):
                arr[i][rit]=c
                c+=1
            rit-=1
            if top<=bot:
                for i in range(rit,let-1,-1):
                    arr[bot][i]=c
                    c+=1
                bot-=1
            if let<=rit:
                for i in range(bot,top-1,-1):
                    arr[i][let]=c
                    c+=1
                let+=1
        return arr