class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result = []
        nums.sort()
        if(nums[0] > 0):
            return []

        for x in range(0,l-1):
            # Since sorted, if curent num is positive no sum can be 0
            if(nums[x] > 0):
                break
            # each iteration should catch the sums for each number therefore if number is same as last num, skip
            if x > 0 and nums[x] == nums[x-1]:
                continue
            else:
                y = x + 1
                z = l-1
                while z > y:
                    sums = (nums[x] + nums[y] + nums[z])
                    # Sum is above 0, need a smaller number
                    if sums > 0:
                        z -= 1
                    # Sum is below 0, need a bigger number
                    elif sums < 0:
                        y += 1
                    # Sum is 0, increment and decrement both to get to new numbers and continue checking 
                    elif sums == 0:
                        result.append([nums[x], nums[y], nums[z]])
                        y += 1
                        z -= 1
                        while nums[y] == nums[y - 1] and z > y:
                            y += 1
        return result




        