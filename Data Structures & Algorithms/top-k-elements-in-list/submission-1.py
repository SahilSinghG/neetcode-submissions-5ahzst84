class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq={}
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        #     freq[nums[i]]=count
        # sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # result=[]
        # for i in range(k):
        #     result.append(sorted_items[i][0])

        # return result
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        buckets = [[] for _ in range(len(nums)+1)]

        for num,count in freq.items():
            buckets[count].append(num)

        result = []

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

                    



