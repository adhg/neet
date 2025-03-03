

class Solution:
    
    def get_unique(self, nums):
        
        if not nums:
            return []
        
        unique = set()
        
        def dfs(L,R):
            if nums[L]==nums[R]:
                unique.add(nums[L]) #add value
                return                    
            
            M = L+(R-L)//2
                 
            #print (f"L:={L}, R:={R}, M:={M}")
            
            dfs(L,M) # go left
            dfs(M+1,R) # go right (NOTE!!! added +1 to void endless loop!)
            
        dfs(L=0,R=len(nums)-1)
        return unique
    
if __name__=='__main__':
    print ("START...")
    
    nums = [1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,5] # + [11]*100_000_000
    print ("X_")
    #print (nums)
    s = Solution()
    n = s.get_unique(nums)
    print ("RES:=",n)
    print ("END")