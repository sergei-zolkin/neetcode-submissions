class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashMap = {letter: s.count(letter) for letter in s}
        t_hashMap = {letter: t.count(letter) for letter in t}

        return s_hashMap == t_hashMap

