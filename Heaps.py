class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,a,n) :
       
        #list containing our min heap.
        min_heap = [] 
    
        #inserting all elements in heap.
        for num in a:
            heapq.heappush(min_heap, num) 
    
        total_cost = 0
    
        #using a loop while there is more than one element in min heap.
        while(len(min_heap)>1): 
            
            #storing the first and second numbers from min heap.
            val_1 = heapq.heappop(min_heap)
            val_2 = heapq.heappop(min_heap)
    
            val = val_1+val_2
            
            #adding their sum in result.
            total_cost+=val
            #pushing the sum first and second numbers in min heap.
            heapq.heappush(min_heap,val)
    
        #returning the result.
        return total_cost