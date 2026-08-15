class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1;
        numOfZero = 0
        result: list = []
        for num in nums:
            if num != 0:
                product *= num 
            else:
                numOfZero += 1           
        for num in nums:
            if numOfZero > 1:
                result.append(0)
            elif num != 0 and numOfZero == 1:
                result.append(0)
            elif num == 0:
                result.append(product)
            else:
                result.append(int(product / num))

        return result
        