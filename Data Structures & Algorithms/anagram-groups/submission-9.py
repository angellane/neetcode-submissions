class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #the 2nd approach is creating a hashmap of the sorted strings, and if the string is already in the hashmap you can add it to that list, if not then a new entry in the map is assigned to that unseen sort

        hashMap = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in hashMap:
                hashMap[sortedS].append(s)
            else:
                hashMap[sortedS] = [s]
        return list(hashMap.values())
                
            
            
        