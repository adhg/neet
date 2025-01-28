# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
         
        dummy = ListNode()
        ptr = dummy
        reminder = 0 
        while l1 or l2 or reminder: #must add remoinder in the event its 8+7
                                                    
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1+v2+reminder
            if total>9:
                reminder = 1
                total = total-10
            else:
                reminder = 0
            
            ptr.next = ListNode(total)             
            
            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
                                                                 
        return dummy.next #we defined a none value node 
    
    


if __name__=='__main__':
    print ("start...")
    
            
    v3 = ListNode(9)
    v4 = ListNode(4,v3)
    v2 = ListNode(2,v4)
    l1 = v2

            
    v4a = ListNode(9)
    v6a = ListNode(6,v4a)
    v5a = ListNode(5,v6a)
    l2 = v5a
    
    s = Solution()
    res = s.addTwoNumbers(l1,l2)
    while res:
        print (res.val)
        res = res.next    
    
    print ("END")