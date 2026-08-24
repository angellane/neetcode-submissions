class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #attempt this problem, there are 2 approaches worth going for
        #the approach by creating a list full of zeros up until 26 for every letter in the alphabet, then when a letter is seen it is incremented, you can then if 2 letter lists are the same and if they are they are anagram 
        #the 2nd approach is creating a hashmap of the sorted strings, and if the string is already in the hashmap you can add it to that list, if not then a new entry in the map is assigned to that unseen sort
        #a similar approach uses defaultdict(list) where you dont have to use the condition statements to alter the structure of the hashmap, it just checks the key of sorted characters and if they match the string is appended to the list and if not then a new entry is made
        result = defaultdict(list)

        for str in strs:
            s = ''.join(sorted(str))
            result[s].append(str)
        return list(result.values())

        
        