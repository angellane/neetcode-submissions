class Solution:
    def isValid(self, s: str) -> bool:
        
        text = []
        for i in s:
            if i == '}':
                if not text or text[-1] != '{':
                    return False
                text.pop()
            elif i == ']':
                if not text or text[-1] != '[':
                    return False
                text.pop()
            elif i == ')':
                if not text or text[-1] != '(':
                    return False
                text.pop()
            else:
                text.append(i)
        return not text
            
