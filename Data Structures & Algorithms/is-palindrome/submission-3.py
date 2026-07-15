class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = []

        for char in s:

            if char.isalnum():

                cleaned.append(char.lower())

        stack = cleaned.copy()

        for char in cleaned:
            if char != stack.pop():
                return False

        return True

