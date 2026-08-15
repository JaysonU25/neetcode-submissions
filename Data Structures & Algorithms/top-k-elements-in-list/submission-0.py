import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        tracker: dict = {}
        l = len(nums)
        if l == k:
            return nums
        
        for i in range(0,l):
            if(tracker.get(nums[i])):
                addi:int = tracker.get(nums[i]) + 1
                tracker[nums[i]] = addi
            else :
                tracker[nums[i]] = 1
            
        items: list = [(v,k) for k,v in tracker.items()]
        heapq.heapify_max(items)

        for i in range(0,k):
            count, num = heapq.heappop_max(items)
            result.append(num)
        return result
        