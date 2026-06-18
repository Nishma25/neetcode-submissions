class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for char in s:
            if char.isalnum():
                word = word + (char.lower())
                print(char)
            else:
                continue
       
        
        if word == word[::-1]:
            return True
        return False
