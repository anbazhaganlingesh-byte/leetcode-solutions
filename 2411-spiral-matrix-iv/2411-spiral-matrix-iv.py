# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        let=0
        rit=n-1
        top=0
        bot=m-1
        curr=head
        arr=[[-1]*n for _ in range(m)]
        while let<=rit and top<=bot:
            for i in range(let,rit+1):
                if curr:
                    arr[top][i]=curr.val
                    curr=curr.next
            top+=1
            for i in range(top,bot+1):
                if curr:
                    arr[i][rit]=curr.val
                    curr=curr.next
            rit-=1
            if top<=bot:
                for i in range(rit,let-1,-1):
                    if curr:
                        arr[bot][i]=curr.val
                        curr=curr.next
                bot-=1
            if top<=bot:
                for i in range(bot,top-1,-1):
                    if curr:
                        arr[i][let]=curr.val
                        curr=curr.next
                let+=1
        return arr
                

