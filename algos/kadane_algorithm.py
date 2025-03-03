
class Solution:
    
    def get_max_array(self,nums):
        
        if not nums:
            return None
        
        local_max = nums[0]
        global_max = local_max
        
        for n in nums[1:]:         
            
            #option 1 (better)
            #local_max = max(n, local_max + n)  # Choose between starting fresh or adding to current subarray
            #global_max = max(global_max, local_max)  # Track the maximum sum seen so far
             
            #option 2  
            if local_max+n>local_max and local_max + n > n:  #note, 2 things MUST happen: (1) you're adding up AND (2) you're bigger than n
                local_max=local_max+n #keep adding            
            else:
                local_max = max(local_max+n,n) #<----------- use only this!
                             
            global_max = max(global_max,local_max)
            
        return global_max
    
if __name__=='__main__':
    print ("START...")
    
    nums = [2, 3, -8, 7, -1, 2, 3] 
    s = Solution()    
    res = s.get_max_array(nums)
    print(res)
    
    print("END")