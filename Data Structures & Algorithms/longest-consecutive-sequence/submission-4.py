import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        current = 1
        last_num: int = None
        num = 0
        if(len(nums) == 0):
            return 0
        heapq.heapify(nums);

        while(nums):
            num = heapq.heappop(nums)
            if(last_num == None or last_num == num):
                last_num = num
                continue
            if(last_num + 1 == num):
                current += 1
                last_num = num
                continue
            else:

                last_num = num
                if(longest < current):
                    longest = current;
                current = 1;
                continue
        if(longest < current):
            longest = current
        return longest
