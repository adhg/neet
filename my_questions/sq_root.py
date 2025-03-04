

class Solution:
    
    def sq_root(self, n):
        
        L = 0
        R = n
        res = 0
        while L<=R:
            
            M = L + ((R-L)//2)
            
            if M**2>n:
                R = M -1
            elif M**2<n:
                L = M + 1
                res = M
            else:
                return M
                
        return res
    
if __name__=='__main__':
    print ("START...")
      
    s = Solution()
    n = s.sq_root(16)
    print ("RES:=",n)
    print ("END")