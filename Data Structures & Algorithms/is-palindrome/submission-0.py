class Solution:
    def isPalindrome(self, s: str) -> bool:
        patched_s = [char.lower() for char in s if char.isdigit() or char.isalpha()]
        for start, char in enumerate(patched_s):
            end = len(patched_s) - 1 - start
            if start > end:
                break
            if char != patched_s[end]:
                return False
        
        return True
