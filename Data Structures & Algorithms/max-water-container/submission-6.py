import heapq
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        max_l = 0
        max_r = 0

        for i in range(len(heights)):
            if(i > 0 and heights[i] <= heights[i-1]):
                continue
            a = heights[i]
            if(a < max_l):
                continue
            for j in range(1,len(heights)-i):
                # if j != len(heights) - 1 and (heights[j] <= heights[j+1]):
                #     continue;
                l = (len(heights) - j)
                b = heights[l]
                if(b < max_r):
                    continue
                volume = (l - i) * min(a, b)
                if volume > max:
                    max = volume
                    max_l = a
                    max_b = b

        return max
