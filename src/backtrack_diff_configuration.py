 

class Solution(object):
    def solve(self, nums):
        
        res = [] 
        combo = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] +=1

        def backtrack(): 
            
            if len(combo)==len(nums):
                res.append(combo[:])
                return

            for n in count:
                if count[n]>0:
                    combo.append(n)
                    count[n]-=1
                    backtrack()
                    count[n]+=1
                    combo.pop()
             

        backtrack()
        return res
        


if __name__=='__main__':
    print ("start...")
    
    s = Solution()
 
    res = s.solve(nums=[1,1,2])
    for r in res:
        print (r)
    
    print ("END")