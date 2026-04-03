class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result=[]
        # visited=[False]*len(strs)
        # for i in range(len(strs)):
        #     if visited[i]:
        #         continue
        #     group=[strs[i]]
        #     visited[i]=True
        #     for j in range(i+1,len(strs)):
        #         if not visited[j] and sorted(strs[i])==sorted(strs[j]):
        #             group.append(strs[j])
        #             visited[j]=True
        #     result.append(group)
        # return result
        hashmap={}
        for word in strs:
            key="".join(sorted(word))
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(word)
        return list(hashmap.values())
        