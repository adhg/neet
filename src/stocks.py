

class Solution(object):
    
    def maxProfit(self, prices):
        
        min_value = prices[0] #maintain min value
        max_value = prices[0] 
        max_profit = 0
        
        for p in prices:            
            min_value = min(min_value, p)
            
            if p>min_value: #the current price must be greater than the already existing min. 
                max_value = max(max_value, p)
            else:
                max_value = p #if not --> theres a new MAX value. Min should always come before Max
            
            max_profit = max(max_profit, max_value-min_value)
        
        return max_profit

if __name__=='__main__':
    print ("START")
    
    prices = [7,1,5,3,6,4,0.5,5]
    s = Solution()
    res = s.maxProfit(prices)
    print ("RES:=",res)
    
    print ("END")