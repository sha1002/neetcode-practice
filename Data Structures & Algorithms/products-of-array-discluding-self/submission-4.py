class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Output = []
        for i in range(len(nums)):
            pdt = 1

            for j in range(len(nums)):
                if i != j:
                    pdt *= nums[j]

            Output.append(pdt)

        return Output
