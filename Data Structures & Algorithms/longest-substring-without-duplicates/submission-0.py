class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

       # for i, c in enumerate(s):
        #    count = 0
         #   if c == s[i-1]:
          #      continue
           # else:
            #    count+=1
       # return count
        l = []
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] != s[j]:
                    l.append([s[i], s[j]])
                else: 
                    return 0
        return len(l)

#initial thoughts ^^^^

#create hashset and go through list checking if element is in the set and if not it is added, if it is in the set, moves to the next iteration and takes the previous subset and the current longest substring in the string 's'

        