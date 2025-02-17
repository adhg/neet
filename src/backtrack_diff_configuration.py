'''
    nums=[1,1,2]
    
    res:
    [1, 1, 2]
    [1, 2, 1]
    [2, 1, 1]
''' 

class Solution(object):
    def solve(self, nums):
        
        res = [] 
        combo = []
        count = {n:0 for n in nums} #you have a counter with KEYS
        for n in nums: 
            count[n] +=1   #you know how manhy KEYS exists (some keys may be duplicated)

        def backtrack(): 
            
            if len(combo)==len(nums):
                res.append(combo[:])
                return

            for n in count:      #iterate the dict with KEYS
                if count[n]>0:  #can I use it? 
                    combo.append(n)  
                    count[n]-=1   #remove from dict so dont reuse if 0
                    backtrack() 
                    count[n]+=1     #add it back
                    combo.pop()   #pop it
             
        backtrack()
        return res
        


if __name__=='__main__':
    print ("start...")
    
    s = Solution()
 
    res = s.solve(nums=[1,1,2])
    for r in res:
        print (r)
    
    print ("END")