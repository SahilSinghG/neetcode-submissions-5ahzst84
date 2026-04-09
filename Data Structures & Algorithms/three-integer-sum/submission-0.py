class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array

        for i in range(len(nums)):
        # If the current number is > 0, the sum can't be 0 (since it's sorted)
            if nums[i] > 0:
                break
        
        # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
        
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1  # Need a larger sum
                elif total > 0:
                    right -= 1 # Need a smaller sum
                else:
                    res.append([nums[i], nums[left], nums[right]])
                
                # Move pointers and skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                
                    left += 1
                    right -= 1
                
        return res
        