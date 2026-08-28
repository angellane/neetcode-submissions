class Solution:
    def isPalindrome(self, s: str) -> bool:
        #create new string removing punctuation
        #add all the chars in string to that 

        newString = ''
        for c in s:
            if c.isalnum():
                newString += c.lower()
    
        return newString == newString[::-1]
        
        