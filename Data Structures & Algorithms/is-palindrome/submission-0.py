class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ''

        for c in s:
            if c.isalnum():
                newString += c.lower()          #stuff has to be lowercase
        return newString == newString[::-1]     
        