class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        if len(nums) < 2:
            return []
        i = 0
        j = 1
        k = 2
        
        if nums[i] + nums[j] + nums[k] == 0:
            result.append([nums[i], nums[j], nums[k]])
        print(result)
        return result
if __name__ == "__main__":
    t1 = [-1,0,1,2,-1,-4]
    s = Solution()
    s.threeSum(t1)
