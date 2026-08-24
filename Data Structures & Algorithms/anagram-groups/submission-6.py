class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #the approach by creating a list full of zeros up until 26 for every letter in the alphabet, then when a letter is seen it is incremented, you can then if 2 letter lists are the same and if they are they are anagram 

        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] +=1

            return result[tuple(count)].append(s)

        return list(result.values())

            
                
            
        