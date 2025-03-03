
# reverse the entire linked list

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
    def __repr__(self):
        return f"value:={self.val}"
    
class Solution(object):
    def reverse(self, head):                
         
        prev = None
        cur = head
        while cur: 
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
              
    
if __name__=='__main__':
    print ("start...")
    
    n8 = ListNode(8)
    n12 = ListNode(12)
    n3 = ListNode(3)
    n17 = ListNode(17)
    n25 = ListNode(25)
    
    n8.next=n12
    n12.next=n3
    n3.next=n17
    n17.next=n25

    
    print ("before...")    
    p = n8
    while p:
        print (p.val,end='-->')
        p=p.next

                        
    s = Solution()
    p = s.reverse(n8)
    print ("\nafter...")    
    while p:
        print (p.val,end='-->')
        p=p.next
        
    print ("\nEND")